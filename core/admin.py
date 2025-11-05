from django.contrib import admin

from .models import (
    Concentration,
    Employer,
    JobPosition,
    JobPositionHighlight,
    Project,
    ProjectRoles,
    ProjectRolesHighlight,
    School,
    Skill,
    SkillCategory,
)

admin.site.register(Employer)
admin.site.register(JobPosition)
admin.site.register(JobPositionHighlight)

admin.site.register(Project)
admin.site.register(ProjectRoles)
admin.site.register(ProjectRolesHighlight)

admin.site.register(SkillCategory)
admin.site.register(Skill)

admin.site.register(School)
admin.site.register(Concentration)
