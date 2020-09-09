from django.core.exceptions import ObjectDoesNotExist

from works.models import Work
from .query_helpers import QueryHelpers as Query

class WorksRepository:
    """
    Data access layer for works
    """

    @staticmethod
    def get_works():
        """
        Returns all works as a list id dict objects.
        """

        sql = """
            select w.*, strftime(w.created_at) as created_at
            from works_work w
            order by created_at desc
        """
        return Query.all(sql)