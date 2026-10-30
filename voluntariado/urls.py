from django.urls import path

from . import views

urlpatterns = [
    path("", views.portada, name="portada"),
    path("oportunidades/", views.ListaOportunidades.as_view(), name="lista_oportunidades"),
    path("oportunidades/<int:pk>/", views.DetalleOportunidad.as_view(), name="detalle_oportunidad"),
    path("causas/", views.ListaCausas.as_view(), name="lista_causas"),
    path("causas/<int:pk>/", views.DetalleCausa.as_view(), name="detalle_causa"),
    path("entidades/", views.ListaEntidades.as_view(), name="lista_entidades"),
    path("entidades/<int:pk>/", views.DetalleEntidad.as_view(), name="detalle_entidad"),
]
