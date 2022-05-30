from django.urls import path
from . import views
urlpatterns = [
    path("years", views.years, name="years"),
    path("lectures/<str:slug>", views.lectures, name="lectures"),
    path("lecture_details/<str:slug>", views.lecture_details, name="lecture_details")
]
