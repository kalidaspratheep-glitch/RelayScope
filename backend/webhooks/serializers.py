from rest_framework import serializers
from .models import WebhookEndpoint, WebhookEvent


class WebhookEndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookEndpoint
        fields = [
            "id",
            "name",
            "token",
            "destination_url",
            "is_active",
            "created_at",
        ]
        read_only_fields = ["id", "token", "created_at"]

from .models import WebhookEvent


class WebhookEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookEvent
        fields = [
            "id",
            "endpoint",
            "method",
            "headers",
            "body",
            "content_type",
            "received_at",
        ]

        read_only_fields = fields