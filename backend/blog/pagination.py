from rest_framework.pagination import CursorPagination


class CustomCursorPagination(CursorPagination):
    page_size = 36
