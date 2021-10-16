from django.urls import path

from .views import (
    UserDetailView,
    InternUpdate,
    InternsView,
    InternDetailView,
    InternStackList,
    JobView,
    JobUpdateView,
    NewsLetterSubscribeView,
    NewsLetterSubscribersView,
    StatisticView,
    StackList,
    total_salary
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
    path("interns/stacks/<int:year>/", StackList.as_view(), name="list_of_stacks_per_year"),
    path("interns/stack/<str:stack>/", InternStackList.as_view(), name="intern_stack"),
    path("interns/total_salary/", total_salary, name="total_salary"),
    path("subscribers/", NewsLetterSubscribersView.as_view(), name="subscribers"),
    path("subscribers/subscribe/", NewsLetterSubscribeView.as_view(), name="subscribe"),
    path("statistics/batch/<int:batch>/", StatisticView.as_view()),
]
