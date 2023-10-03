from django.urls import path

from .import views

urlpatterns = [
    path("", views.myname, name = "myname"),
]