from django.contrib import admin

from .models import Program, ProgramAssignment


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'duration_weeks', 'estimated_session_minutes')
    search_fields = ('name',)
    list_filter = ('level',)


@admin.register(ProgramAssignment)
class ProgramAssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'program', 'status', 'start_date', 'end_date')
    search_fields = ('user__email', 'program__name')
    list_filter = ('status',)
