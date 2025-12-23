from django.contrib import admin

from .models import UserSubscription


@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'plan_name', 'status', 'auto_renew', 'expires_at')
    search_fields = ('user__email', 'plan_name')
    list_filter = ('status', 'auto_renew')
