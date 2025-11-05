from django.db import models

DEFAULT_DATE = "9999-12-31"


class NamedEntity(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name
