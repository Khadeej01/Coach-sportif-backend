from rest_framework import permissions, viewsets

from .models import OnboardingProfile
from .serializers import OnboardingProfileSerializer


class OnboardingProfileViewSet(viewsets.ModelViewSet):
    serializer_class = OnboardingProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return OnboardingProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
