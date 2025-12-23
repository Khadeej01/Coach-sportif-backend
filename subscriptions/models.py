from django.conf import settings
from django.db import models


class UserSubscription(models.Model):
    STATUS_CHOICES = [
        ('inactive', 'Inactive'),
        ('active', 'Active'),
        ('cancelled', 'Cancelled'),
        ('past_due', 'Past due'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions')
    plan_name = models.CharField(max_length=64, default='free')
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='inactive')
    started_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    auto_renew = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user} - {self.plan_name} ({self.status})"

    class Meta:
        ordering = ['-started_at']
