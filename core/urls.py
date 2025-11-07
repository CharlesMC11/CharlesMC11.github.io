from django.urls import path

from . import views

urlpatterns = (
    path("", views.index, name="index"),
    path("3d/", views.three_d, name="3d"),
    path("photo/", views.photography, name="photography"),
    path("cv/", views.cv, name="cv"),
    path("about-me/", views.about_me, name="about-me"),
)
