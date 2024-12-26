from rest_framework.pagination import LimitOffsetPagination

class FileLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 100


from rest_framework.pagination import PageNumberPagination

class FolderPageNumberPagination(PageNumberPagination):
    page_size = 10
