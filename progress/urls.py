from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import WorkoutSessionViewSet

router = DefaultRouter()
router.register(r'workout-sessions', WorkoutSessionViewSet, basename='workout-session')

urlpatterns = [
    path('', include(router.urls)),
]

