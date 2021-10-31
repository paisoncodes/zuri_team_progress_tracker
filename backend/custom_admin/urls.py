from app import views
from django.urls import path

from custom_admin.views import (ChangePasswordView, CustomAuthToken,
                                InternAdminUpdateView, InternsAdminView,
                                StackAdminCreateView, StackAdminUpdateView,
                                UserAdminCreateView, UserAdminUpdateView)

urlpatterns = [
    # ================================================================================================================
    path("users/", UserAdminCreateView.as_view(), name="UserCreate"),
    path("users/<str:user_id>/", UserAdminUpdateView.as_view(), name="UserUpdate"),
    # ================================================================================================================
    path("stacks/", StackAdminCreateView.as_view(), name="StackCreate"),
    path("stacks/<int:stack_id>/", StackAdminUpdateView.as_view(), name="StackUpdate"),
    # ================================================================================================================
    path("interns/", views.InternsView.as_view(), name="InternCreate"),
    path("interns/<str:intern_id>/update/", InternAdminUpdateView.as_view(), name="InternUpdate"),
    path('change_password/', ChangePasswordView.as_view(), name='auth_change_password'),
    # ================================================================================================================
    path(r'login/', CustomAuthToken.as_view())
    # ================================================================================================================
]
