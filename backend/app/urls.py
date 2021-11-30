from django.urls import path

from .data import create_an_intern, create_stacks, create_stat
from .views import (
    BatchList,
    GetStacksPerBatch,
    InternDetailView,
    InternStackList,
    InternsView,
    InternUpdate,
    JobUpdateView,
    JobView,
    NewsLetterSubscribersView,
    NewsLetterSubscribeView,
    Search,
    SponsorView,
    StatisticView,
    all_stats,
    get_all_jobs,
    get_interns_by_year_and_stack,
    total_salary,
    test,
    home
)

urlpatterns = [
    # ================================================================================================================
    path("interns/<str:intern_id>/", InternDetailView.as_view(), name="Intern_detail"),
    path("interns/<str:intern_id>/jobs/", JobView.as_view(), name="job"),
    path(
        "interns/<str:intern_id>/jobs/<str:job_id>/",
        JobUpdateView.as_view(),
        name="job_update",
    ),
    path(
        "interns/<str:intern_id>/update/", InternUpdate.as_view(), name="intern_update"
    ),
    path("interns/", InternsView.as_view(), name="intern_list"),
    path("interns/stack/<str:stack>/", InternStackList.as_view(), name="intern_stack"),
    path("interns/batch/<int:batch>/total_salary/", total_salary, name="total_salary"),
    path(
        "interns/batch/<int:batch>/",
        BatchList.as_view(),
        name="list_of_interns_per_batch",
    ),
    path(
        "interns/batch/<int:batch>/stack/<str:stack>/",
        get_interns_by_year_and_stack,
        name="stack_list_and_count",
    ),
    # ================================================================================================================
    path("stacks/batch/<int:batch>/", GetStacksPerBatch.as_view(), name="get_stats"),
    path("subscribers/", NewsLetterSubscribersView.as_view(), name="subscribers"),
    path("subscribers/subscribe/", NewsLetterSubscribeView.as_view(), name="subscribe"),
    # ================================================================================================================
    path("statistics/batch/<int:batch>/", StatisticView.as_view()),
    path("statistics/", all_stats, name="all_stats"),
    # ================================================================================================================
    path("sponsors/", SponsorView.as_view()),
    path("sponsors/<str:id>/", SponsorView.as_view()),
    path("populate/interns/", create_an_intern),
    path("populate/stacks/", create_stacks),
    path("populate/statistics/", create_stat),
    path("tistic/", get_all_jobs),
    path("search/", Search.as_view(), name="search"),
    path("test", test),
    path("", home, name="homepage"),
]
