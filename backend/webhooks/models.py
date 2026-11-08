import uuid

from django.db import models


class WebhookEndpoint(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(max_length=100)

    token = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    destination_url = models.URLField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class WebhookEvent(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    endpoint = models.ForeignKey(
        WebhookEndpoint,
        on_delete=models.CASCADE,
        related_name="events"
    )

    method = models.CharField(max_length=10)

    headers = models.JSONField(default=dict)

    body = models.TextField(blank=True)

    content_type = models.CharField(
        max_length=255,
        blank=True
    )

    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.method} - {self.endpoint.name}"

class DeliveryAttempt(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    event = models.ForeignKey(
        WebhookEvent,
        on_delete=models.CASCADE,
        related_name="attempts"
    )

    attempted_at = models.DateTimeField(auto_now_add=True)

    status_code = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )

    response_body = models.TextField(blank=True)

    success = models.BooleanField(default=False)

    error_message = models.TextField(blank=True)

    duration_ms = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Attempt for {self.event_id}"