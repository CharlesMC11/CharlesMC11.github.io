from django.urls import path

from . import views

urlpatterns = (
    path("", views.index, name="index"),
    path("projects/", views.projects, name="projects"),
    path("resume/", views.resume, name="resume"),
    path("about/", views.about, name="about"),
)
