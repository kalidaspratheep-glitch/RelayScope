# RelayScope

**Webhook Inspection, Debugging & Replay Platform**

RelayScope is a developer tool for capturing, inspecting, and replaying webhook events. It helps developers debug webhook integrations by storing incoming requests and allowing them to be forwarded to a configured destination.

## Features

- Create webhook endpoints with unique tokens.
- Capture incoming HTTP webhook requests.
- Store request headers, body, method, content type, and timestamp.
- Retrieve events for an endpoint, ordered by newest first.
- Replay captured events to a configured destination URL.
- Track delivery attempts, response status, execution time, and errors.
- Handle successful deliveries and connection failures.

## Tech Stack

- **Backend:** Python, Django, Django REST Framework
- **Database:** PostgreSQL
- **Database setup:** Docker Compose
- **HTTP requests:** Requests
- **Configuration:** python-dotenv

## How It Works

1. A developer creates a webhook endpoint in RelayScope.
2. RelayScope generates a unique token and webhook URL.
3. An external service sends webhook events to that URL.
4. RelayScope captures and stores the incoming request.
5. The developer retrieves and inspects captured events.
6. The developer can replay an event to a configured destination URL.
7. RelayScope records the delivery result, including response status, duration, and errors.

## Getting Started

### Prerequisites

- Python 3.10+
- Docker Desktop with Docker Compose
- Git

### 1. Clone the repository

```bash
git clone <repository-url>
cd RelayScope
