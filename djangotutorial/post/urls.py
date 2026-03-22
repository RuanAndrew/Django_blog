from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path("", views.list, name="list"),
    path("<int:post_id>/", views.details, name="details"),
]