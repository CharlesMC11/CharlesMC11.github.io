from django.db import models

from .base import DEFAULT_DATE, NamedEntity


class Employer(NamedEntity):
    location = models.CharField(max_length=50, blank=False)

    class Meta:
        ordering = ["-jobposition__end_date", "-jobposition__start_date"]
        verbose_name_plural = "JOB - Employers"


class JobPosition(NamedEntity):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False, default=DEFAULT_DATE)

    class Meta:
        ordering = ["-end_date", "-start_date"]
        verbose_name_plural = "JOB - Positions"


class JobPositionHighlight(models.Model):
    position = models.ForeignKey(JobPosition, on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "JOB - Position Highlights"

    def __str__(self) -> str:
        return self.description
