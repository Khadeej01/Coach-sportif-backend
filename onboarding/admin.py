from django.contrib import admin

from .models import OnboardingProfile


@admin.register(OnboardingProfile)
class OnboardingProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'sport_level', 'primary_goal', 'time_per_week', 'equipment')
    search_fields = ('user__email', 'user__username')
