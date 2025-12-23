from django.conf import settings
from django.db import models


class WorkoutSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='workout_sessions')
    program_assignment = models.ForeignKey(
        'workouts.ProgramAssignment',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sessions',
    )
    performed_at = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(default=0)
    calories_estimated = models.PositiveIntegerField(null=True, blank=True)
    completed = models.BooleanField(default=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Session {self.id} - {self.user}"

    class Meta:
        ordering = ['-performed_at']
