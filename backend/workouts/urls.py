from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProgramAssignmentViewSet, ProgramViewSet

router = DefaultRouter()
router.register(r'programs', ProgramViewSet, basename='program')
router.register(r'program-assignments', ProgramAssignmentViewSet, basename='program-assignment')

urlpatterns = [
    path('', include(router.urls)),
]

