from rest_framework import permissions, viewsets

from .models import WorkoutSession
from .serializers import WorkoutSessionSerializer


class WorkoutSessionViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WorkoutSession.objects.filter(user=self.request.user).select_related('program_assignment')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
