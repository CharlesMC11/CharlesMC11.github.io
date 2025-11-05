from django.db import models

from .base import DEFAULT_DATE, NamedEntity


class Project(NamedEntity):
    type = models.CharField(max_length=50, blank=False)
    link = models.URLField(null=True)

    class Meta:
        ordering = ["-projectroles__end_date", "-projectroles__start_date"]
        verbose_name_plural = "PRJ - Projects"


class ProjectRoles(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    roles = models.CharField(max_length=100, blank=False)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False, default=DEFAULT_DATE)

    class Meta:
        ordering = ["-end_date", "-start_date"]
        verbose_name_plural = "PRJ - Roles"

    def __str__(self) -> str:
        return self.roles


class ProjectRolesHighlight(models.Model):
    roles = models.ForeignKey(ProjectRoles, on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "PRJ - Roles Highlights"

    def __str__(self) -> str:
        return self.description
