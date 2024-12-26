from .pagination import FileLimitOffsetPagination,FolderPageNumberPagination
from .models import File,Folder
from .serializers import FolderSerializer,FileSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['created_at','id']
    search_fields = ['^name','=id']
    ordering = ['created_at','id']
    ordering_fields = ['created_at','id']
    pagination_class = FileLimitOffsetPagination

class FolderViewSet(ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = FolderPageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['created_at','id']
    search_fields = ['^name','=id']
    ordering = ['created_at','id']
    ordering_fields = ['created_at','id']