import json
from django.http import HttpResponse
from django.views.generic import View

from repositories.works_repository import WorksRepository as repo

class GetWorks(View):
    """
    Returns works.
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse(json.dumps(repo.get_works()), content_type="application/json")



