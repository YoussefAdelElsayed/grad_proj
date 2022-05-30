from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView


urlpatterns = [
    path("overview", views.overview, name="overview"),
    path("show_posts", views.show_posts, name="show_posts"),
    path("show_doctors", views.show_doctors, name="show_doctors"),
    path("show_asks", views.show_asks, name="show_asks"),
    path("show_lectures", views.show_lectures, name="show_lectures"),
    path("add_post", views.add_post, name="add_post"),
    path("add_lecture", views.add_lecture, name="add_lecture"),
    path("add_doctor", views.add_doctor, name="add_doctor"),
    path("update_post/<int:id>", views.update_post, name="update_post"),
    path("update_doctor/<int:id>", views.update_doctor, name="update_doctor"),
    path("update_lecture/<int:id>", views.update_lecture, name="update_lecture"),
    path("answer_ask/<int:id>", views.answer_ask, name="answer_ask"),
    path("department", views.department, name="department"),
    path("edit_home", views.edit_home, name="edit_home"),
]



