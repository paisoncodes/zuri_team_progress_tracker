"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.urls.conf import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from django.views.generic import TemplateView


schema_view = get_schema_view(
    openapi.Info(
        title="Progress Tracker API",
        default_version="1.0.0",
        description="Tracks the progress of past interns",
    ),
    url="https://progress.zuri.team",
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("app.urls")),
    path("api/v1/admin/", include("custom_admin.urls")),
    path("", TemplateView.as_view(template_name="index.html"))
]


urlpatterns += [
    url(
        r"^swagger(?P<format>\.json|\.yaml)$",
        csrf_exempt(schema_view.without_ui(cache_timeout=0)),
        name="schema-json",
    ),
    url(
        r"^api/v1/docs/$",
        csrf_exempt(schema_view.with_ui("swagger", cache_timeout=0)),
        name="schema-swagger-ui",
    ),
    url(
        r"^redoc/$", csrf_exempt(schema_view.with_ui("redoc", cache_timeout=0)), name="schema-redoc"
    ),
]
