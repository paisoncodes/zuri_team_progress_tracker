from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from rest_framework import permissions
from .views import (
    UserCreateView,
    UserUpdateView,
    UserDetailView,

    InternCreateUpdateView,
    InternList,
    InternDetailView,

    JobView,
    JobUpdateView,


    NewsLetterSubscribeView,
    NewsLetterSubscribersView
)



urlpatterns = [
    path("users/create/",UserCreateView.as_view(),name="create_user"),
    path("users/update/<int:user_id>/",UserUpdateView.as_view(),name="update_user"),
    path("intern/<int:pk>/", InternDetailView.as_view(), name="Intern_detail"),
    path("users/<int:user_id>/", UserDetailView.as_view(), name="UserInfo"),
    path("interns/<str:username>/jobs/", JobView.as_view(), name="job"),
    path("interns/<str:username>/jobs/<int:pk>/", JobUpdateView.as_view(), name="job_update"),
    path('intern/create/', InternCreateUpdateView.as_view(), name='intern_create_update'),
    path('interns/', InternList.as_view(), name='intern_list'),
    path("subscribers/", NewsLetterSubscribersView.as_view(), name="subscribers"),
    path("subscribers/subscribe/", NewsLetterSubscribeView.as_view(),name="subscribe"),
    
] 

