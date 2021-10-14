from .import views

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework import permissions
from app import views
from .views import UserListView, UserCreateView, UserUpdateView


urlpatterns = [
    path("users/create/",UserCreateView.as_view(),name="create_user"),
    path("users/update/<int:user_id>/",UserUpdateView.as_view(),name="update_user"),
    path("users/<int:user_id>", UserListView.as_view(), name="UserInfo"),
    path("jobs/create/<str:username>/", views.JobView.as_view(), name="Jobcreate"),

    path("interns/update/<int:pk>/", views.InternDetailView.as_view())
] 

