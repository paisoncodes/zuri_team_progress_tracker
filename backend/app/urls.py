from django.urls import path

# from django.conf import settings
# from django.conf.urls.static import static
# from rest_framework import
from . import views
from .views import (
    UserCreateView,
    UserUpdateView,
    UserDetailView,
    InternCreateUpdateView,
    InternUpdate,
    InternsView,
    InternDetailView,
    InternStackList,
    JobView,
    JobUpdateView,
    NewsLetterSubscribeView,
    NewsLetterSubscribersView,
    StatisticView,
)


urlpatterns = [
    path("interns/<int:pk>/", InternDetailView.as_view(), name="Intern_detail"),
    path("users/<int:user_id>/", UserDetailView.as_view(), name="UserInfo"),
    path("interns/<int:intern_id>/jobs/", JobView.as_view(), name="job"),
    path(
        "interns/<int:intern_id>/jobs/<int:pk>/",
        JobUpdateView.as_view(),
        name="job_update",
    ),
    path(
        "interns/<int:intern_id>/update", InternUpdate.as_view(), name="intern_update"
    ),
    path("interns/", InternsView.as_view(), name="intern_list"),
    path("interns/stack/<str:stack>/", InternStackList.as_view(), name="intern_stack"),
    path("interns/total_salary", views.total_salary, name="totalsal"),
    path("subscribers/", NewsLetterSubscribersView.as_view(), name="subscribers"),
    path("subscribers/subscribe/", NewsLetterSubscribeView.as_view(), name="subscribe"),
    path("statistics/batch/<int:batch>/", StatisticView.as_view()),
]
