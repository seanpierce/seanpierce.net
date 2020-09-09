from pages.models import Page
from .query_helpers import QueryHelpers as Query

class PagesRepository:
    """
    Data access layer for works
    """

    @staticmethod
    def get_contact_page():
        """
        Returns contact page content.
        """

        sql = """
            select 
                p.*, 
                strftime(p.created_at) as created_at
            from pages_page p
            where p.title = 'Contact'
        """
        return Query.single(sql)