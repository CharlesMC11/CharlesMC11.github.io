from django.db import models

from .base import NamedEntity


class SkillCategory(NamedEntity):
    class Meta:
        verbose_name_plural = "SKL - Skill Categories"


class Skill(NamedEntity):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=50)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", 'subcategory']
        verbose_name_plural = "SKL - Skills"
