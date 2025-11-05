from django.db import models

from .base import DEFAULT_DATE, NamedEntity


class School(NamedEntity):
    location = models.CharField(max_length=50, blank=False)

    class Meta:
        ordering = ["-concentration__awarded"]
        verbose_name_plural = "EDU - Schools"


class Concentration(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    degree = models.CharField(max_length=50, blank=True)
    concentration = models.CharField(max_length=50, blank=True)
    awarded = models.DateField(blank=False, default=DEFAULT_DATE)

    class Meta:
        ordering = ["-awarded"]
        verbose_name_plural = "EDU - Concentrations"

    def __str__(self):
        return f"{self.degree} in {self.concentration}"
