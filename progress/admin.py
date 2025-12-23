from django.contrib import admin

from .models import WorkoutSession


@admin.register(WorkoutSession)
class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'program_assignment', 'performed_at', 'duration_minutes', 'completed')
    search_fields = ('user__email',)
    list_filter = ('completed',)
