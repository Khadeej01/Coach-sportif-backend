from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RegistrationView, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('auth/register/', RegistrationView.as_view(), name='auth-register'),
    path('', include(router.urls)),
]

