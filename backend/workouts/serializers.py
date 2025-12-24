from rest_framework import serializers

from .models import Program, ProgramAssignment


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = [
            'id',
            'name',
            'description',
            'level',
            'duration_weeks',
            'estimated_session_minutes',
            'equipment',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ProgramAssignmentSerializer(serializers.ModelSerializer):
    program_detail = ProgramSerializer(source='program', read_only=True)

    class Meta:
        model = ProgramAssignment
        fields = [
            'id',
            'program',
            'program_detail',
            'status',
            'start_date',
            'end_date',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

