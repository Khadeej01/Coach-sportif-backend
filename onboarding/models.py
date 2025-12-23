from django.conf import settings
from django.db import models


class OnboardingProfile(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    GOAL_CHOICES = [
        ('weight_loss', 'Weight loss'),
        ('muscle_gain', 'Muscle gain'),
        ('general_fitness', 'General fitness'),
    ]

    EQUIPMENT_CHOICES = [
        ('none', 'No equipment'),
        ('basic', 'Basic equipment'),
        ('full', 'Full gym access'),
    ]

    SPACE_CHOICES = [
        ('small', 'Small space'),
        ('medium', 'Medium space'),
        ('large', 'Large space'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='onboarding')
    sport_level = models.CharField(max_length=32, choices=LEVEL_CHOICES)
    primary_goal = models.CharField(max_length=32, choices=GOAL_CHOICES)
    time_per_week = models.PositiveIntegerField(default=3)
    equipment = models.CharField(max_length=32, choices=EQUIPMENT_CHOICES, default='basic')
    space = models.CharField(max_length=32, choices=SPACE_CHOICES, default='medium')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Onboarding for {self.user}"

    class Meta:
        ordering = ['-created_at']
