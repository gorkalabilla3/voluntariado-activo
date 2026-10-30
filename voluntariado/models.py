from django.db import models
from django.urls import reverse


class Causa(models.Model):
    """Causa a la que se dirige una oportunidad (infancia, medio ambiente...)."""

    nombre = models.CharField(max_length=60, unique=True)
    descripcion = models.TextField("descripción")

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("detalle_causa", args=[self.pk])


class Entidad(models.Model):
    """ONG o entidad que organiza oportunidades de voluntariado."""

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField("descripción")
    web = models.URLField(blank=True)
    email = models.EmailField("correo de contacto", blank=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "entidades"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("detalle_entidad", args=[self.pk])


class Oportunidad(models.Model):
    """Oportunidad de voluntariado.

    - Pertenece a UNA causa (ForeignKey -> relación 1:N).
    - Puede estar organizada por VARIAS entidades y una entidad organiza
      varias oportunidades (ManyToManyField -> relación N:M).
    Con related_name="oportunidades" podemos escribir causa.oportunidades.all()
    y entidad.oportunidades.all() desde el otro lado de la relación.
    """

    titulo = models.CharField("título", max_length=150)
    descripcion = models.TextField("descripción")
    causa = models.ForeignKey(Causa, on_delete=models.PROTECT, related_name="oportunidades")
    entidades = models.ManyToManyField(Entidad, related_name="oportunidades")
    lugar = models.CharField(max_length=100)
    fecha_inicio = models.DateField("fecha de inicio")
    fecha_fin = models.DateField("fecha de fin", blank=True, null=True)
    horas_semana = models.PositiveSmallIntegerField("horas por semana")
    plazas = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["fecha_inicio", "titulo"]
        verbose_name_plural = "oportunidades"

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("detalle_oportunidad", args=[self.pk])
