from collections import OrderedDict

from rest_framework import pagination

from api.http import Response


class PageNumberPagination(pagination.PageNumberPagination):

    # Allow client-side to declare page size
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('num_pages', self.page.paginator.num_pages),
            ('results', data),
            ('current', self.page.number)
        ]))
