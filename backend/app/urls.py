from django.urls import path
from django.contrib import admin


from .views import (
    InternUpdate,
    InternsView,
    InternDetailView,
    InternStackList,
    JobView,
    JobUpdateView,
    NewsLetterSubscribeView,
    NewsLetterSubscribersView,
    StatisticView,
    BatchList,
    all_stats,
    get_interns_by_year_and_stack,
    total_salary,
    SponsorView,
    search,
)
from app import views

from . import data


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
        views.get_interns_by_year_and_stack,
        name="stack_list_and_count",
    ),
    # ================================================================================================================
    path(
        "stacks/batch/<int:batch>/", views.GetStacksPerBatch.as_view(), name="get_stats"
    ),
    path("subscribers/", NewsLetterSubscribersView.as_view(), name="subscribers"),
    path("subscribers/subscribe/", NewsLetterSubscribeView.as_view(), name="subscribe"),
    # ================================================================================================================
    path("statistics/batch/<int:batch>/", StatisticView.as_view()),
    path("statistics/", views.all_stats, name="all_stats"),
    # ================================================================================================================
    path("sponsors/", SponsorView.as_view()),
    path("sponsors/<str:id>/", SponsorView.as_view()),
    path("populate_interns/", data.create_an_intern),
    path("populate_stacks/", data.create_stacks),
    path("populate_statistic/", data.create_stat),
    path("tistic/", views.get_all_jobs),
    path("search/", search.as_view(), name="search"),
]

