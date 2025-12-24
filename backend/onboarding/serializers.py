from rest_framework import serializers

from .models import OnboardingProfile


class OnboardingProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnboardingProfile
        fields = [
            'id',
            'sport_level',
            'primary_goal',
            'time_per_week',
            'equipment',
            'space',
            'notes',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

