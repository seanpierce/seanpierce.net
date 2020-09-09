from django.urls import path, include

from .works_api import GetWorks

urlpatterns = [
    path('works', GetWorks.as_view())
]