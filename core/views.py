from django.db.models import Model, Prefetch
from django.shortcuts import render

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


def index(request):
    return render(request, "core/index.html")


def three_d(request):
    return render(request, "core/3d.html")


def photography(request):
    return render(request, "core/photography.html")


def cv(request):
    def get_highlights(
        primary_model: Model, secondary_model: Model, tertiary_model: Model
    ) -> dict[Model, dict[Model, list[Model]]]:
        def get_reverse_many_to_one_descriptor_str(model: Model) -> str:
            """Get the reverse many-to-one descriptor of a model.

            :param model: a Django model
            :returns: the reverse many-to-one descriptor as a string
            """

            return f"{model.__name__.lower()}_set"

        secondary_reverse_many_to_one_descriptor_str = (
            get_reverse_many_to_one_descriptor_str(secondary_model)
        )
        tertiary_reverse_many_to_one_descriptor_str = (
            get_reverse_many_to_one_descriptor_str(tertiary_model)
        )

        query = primary_model.objects.prefetch_related(
            Prefetch(
                secondary_reverse_many_to_one_descriptor_str,
                queryset=secondary_model.objects.prefetch_related(
                    tertiary_reverse_many_to_one_descriptor_str
                ),
            )
        )

        result: dict[Model, dict[Model, list[Model]]] = {}
        for entity in query:
            if entity in result:
                continue

            result[entity] = {}
            for role in getattr(
                entity, secondary_reverse_many_to_one_descriptor_str
            ).all():
                if role in result[entity]:
                    continue

                result[entity][role] = [
                    highlight
                    for highlight in getattr(
                        role, tertiary_reverse_many_to_one_descriptor_str
                    ).all()
                ] or None

        return result

    experience: dict[
        Employer, dict[JobPosition, list[JobPositionHighlight]]
    ] = get_highlights(Employer, JobPosition, JobPositionHighlight)

    projects: dict[Project, dict[ProjectRoles, list[ProjectRolesHighlight]]] = (
        get_highlights(Project, ProjectRoles, ProjectRolesHighlight)
    )

    skills_query = SkillCategory.objects.prefetch_related("skill_set")
    skills: dict[SkillCategory, list[Skill]] = {}
    for category in skills_query:
        if category in skills:
            continue

        skills[category] = []
        for skill in category.skill_set.all():
            if skill in skills[category]:
                continue

            skills[category].append(skill)

    education_query = School.objects.prefetch_related("concentration_set")
    education: dict[School, list[Concentration]] = {}
    for school in education_query:
        if school in education:
            continue

        education[school] = []
        for concentration in school.concentration_set.all():
            if concentration in education[school]:
                continue

            education[school].append(concentration)

    context = {
        "experience": experience,
        "projects": projects,
        "skills": skills,
        "education": education,
    }
    return render(request, "core/cv/base.html", context)


def about_me(request):
    return render(request, "core/about-me.html")
