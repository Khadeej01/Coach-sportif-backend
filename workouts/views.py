from rest_framework import permissions, viewsets

from .models import Program, ProgramAssignment
from .serializers import ProgramAssignmentSerializer, ProgramSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProgramAssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = ProgramAssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ProgramAssignment.objects.filter(user=self.request.user).select_related('program')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
