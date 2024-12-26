from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import FolderViewSet,FileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'files',FileViewSet)
router.register(r'folders',FolderViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += router.urls