from django.urls import path
from .views import WebhookEndpointListCreateView, WebhookReceiveView, WebhookEventListView, WebhookReplayView

urlpatterns = [
    path(
        "endpoints/",
        WebhookEndpointListCreateView.as_view(),
        name="endpoint-list-create",
    ),
    path(
        "hooks/<uuid:token>/",
        WebhookReceiveView.as_view(),
        name="webhook-receive",
    ),
    path(
        "endpoints/<uuid:endpoint_id>/events/",
        WebhookEventListView.as_view(),
        name="endpoint-events",
    ),
    path(
        "events/<uuid:event_id>/replay/",
        WebhookReplayView.as_view(),
        name="event-replay",
    ),
]