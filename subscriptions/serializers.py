from rest_framework import serializers

from .models import UserSubscription


class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = [
            'id',
            'plan_name',
            'status',
            'started_at',
            'expires_at',
            'auto_renew',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'started_at', 'created_at', 'updated_at']

