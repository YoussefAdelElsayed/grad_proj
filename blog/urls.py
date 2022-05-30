from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dean", views.dean, name="dean"),
    path("posts", views.all_posts, name="all_posts"),
    path("post/<int:id>", views.post_details, name="post_details")
]
