import json
from django.http import HttpResponse
from django.views.generic import View

from repositories.pages_repository import PagesRepository as repo

class GetConactPage(View):
    """
    Returns contnet for the contact page.
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse(json.dumps(repo.get_contact_page()), content_type="application/json")



