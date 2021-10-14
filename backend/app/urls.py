from django.urls import path
from rest_framework import permissions
from app import views
from .views import UserClassView


urlpatterns = [
    path("users/<int:pk>/", views.UserClassView.as_view(), name="UserInfo"),

]