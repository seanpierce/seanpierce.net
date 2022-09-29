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
            select 
                w.*, 
                strftime(w.created_at) as created_at,
                (select group_concat(image) from works_workimage where work_id = w.id) as images
            from works_work w
            order by 
            present desc,
            year desc
        """
        return Query.all(sql)