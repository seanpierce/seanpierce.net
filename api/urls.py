from django.urls import path, include

from .works_api import GetWorks
from .pages_api import GetConactPage

urlpatterns = [
    path('works', GetWorks.as_view()),
    path('pages/contact', GetConactPage.as_view())
]