from django.db.models import Count
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import DetailView, ListView

from .models import Causa, Entidad, Oportunidad


def portada(request):
    """Muestra una oportunidad por cada causa.

    Criterio: la próxima oportunidad que empieza a partir de hoy. Si una causa
    no tiene ninguna futura, se muestra la más reciente para que no quede vacía.
    """
    hoy = timezone.localdate()
    destacadas = []
    for causa in Causa.objects.all():
        oportunidades = causa.oportunidades.prefetch_related("entidades")
        oportunidad = (
            oportunidades.filter(fecha_inicio__gte=hoy).order_by("fecha_inicio").first()
            or oportunidades.order_by("-fecha_inicio").first()
        )
        if oportunidad:
            destacadas.append(oportunidad)
    destacadas.sort(key=lambda o: o.fecha_inicio)
    # para sacar cuantas oportunidades tiene cada causa
    causas = Causa.objects.annotate(num_oportunidades=Count("oportunidades"))
    contexto = {"destacadas": destacadas, "causas": causas}
    return render(request, "voluntariado/portada.html", contexto)


# Vistas genéricas: Django busca la plantilla <app>/<modelo>_list.html y
# <app>/<modelo>_detail.html y pasa los objetos como object_list / object.
# Con context_object_name les damos un nombre más legible.

class ListaOportunidades(ListView):
    queryset = Oportunidad.objects.select_related("causa").prefetch_related("entidades")
    context_object_name = "oportunidades"


class DetalleOportunidad(DetailView):
    queryset = Oportunidad.objects.select_related("causa").prefetch_related("entidades")
    context_object_name = "oportunidad"


class ListaCausas(ListView):
    model = Causa
    context_object_name = "causas"


class DetalleCausa(DetailView):
    model = Causa
    context_object_name = "causa"


class ListaEntidades(ListView):
    model = Entidad
    context_object_name = "entidades"


class DetalleEntidad(DetailView):
    model = Entidad
    context_object_name = "entidad"
