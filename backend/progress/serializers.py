from rest_framework import serializers

from .models import WorkoutSession


class WorkoutSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSession
        fields = [
            'id',
            'program_assignment',
            'performed_at',
            'duration_minutes',
            'calories_estimated',
            'completed',
            'notes',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

