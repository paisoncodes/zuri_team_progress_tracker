from django.urls import path

from custom_admin.views import (
    UserAdminCreateView,
    UserAdminUpdateView
)

from app import views


urlpatterns = [
    # ================================================================================================================
    path("users/", UserAdminCreateView.as_view(), name="UserCreate"),
    path("users/<str:user_id>/", UserAdminUpdateView.as_view(), name="UserUpdate"),
    # ================================================================================================================
]