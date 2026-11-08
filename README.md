
# RelayScope

**Webhook Inspection, Debugging & Replay Platform**

RelayScope is a developer tool for capturing, inspecting, and replaying webhook events. It helps developers debug webhook integrations by storing incoming requests and allowing them to be forwarded to a configured destination.

## Features

- Create webhook endpoints with unique tokens.
- Capture incoming HTTP webhook requests.
- Store request headers, body, HTTP method, content type, and timestamp.
- Retrieve events for an endpoint, ordered by newest first.
- Replay captured events to a configured destination URL.
- Track delivery attempts, response status, execution time, and errors.
- Handle successful deliveries and connection failures.

## Tech Stack

- **Backend:** Python, Django, Django REST Framework
- **Database:** PostgreSQL
- **Database Setup:** Docker Compose
- **HTTP Requests:** Requests
- **Configuration:** python-dotenv

## How It Works

1. A developer creates a webhook endpoint in RelayScope.
2. RelayScope generates a unique token and webhook URL.
3. An external service sends webhook events to that URL.
4. RelayScope captures and stores the incoming request, including its headers and payload.
5. The developer retrieves and inspects captured events.
6. The developer can replay an event to a configured destination URL.
7. RelayScope records the delivery result, including response status, duration, and errors.

## Getting Started

### Prerequisites

- Python 3.12+
- Docker Desktop with Docker Compose
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/kalidaspratheep-glitch/RelayScope.git
cd RelayScope
```

### 2. Start PostgreSQL

```bash
docker compose up -d
```

### 3. Set Up the Backend

```bash
cd backend
python -m venv .venv
```

Activate the virtual environment.

**Windows (Git Bash / MSYS2):**

```bash
source .venv/Scripts/activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the example environment file:

```bash
cp .env.example .env
```

Update the values in `.env` if your local PostgreSQL configuration differs.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

The backend will be available at:

`http://127.0.0.1:8000/`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/endpoints/` | List webhook endpoints |
| POST | `/api/endpoints/` | Create a webhook endpoint |
| POST | `/api/hooks/<token>/` | Receive an incoming webhook |
| GET | `/api/endpoints/<endpoint_id>/events/` | List events for an endpoint |
| POST | `/api/events/<event_id>/replay/` | Replay a captured event |

## Example: Send a Webhook

Replace `<token>` with the token returned when creating an endpoint.

```bash
curl -X POST http://127.0.0.1:8000/api/hooks/<token>/ \
  -H "Content-Type: application/json" \
  -H "X-Test-Source: RelayScope" \
  -d '{"event": "payment.succeeded", "amount": 1000, "currency": "USD"}'
```

RelayScope captures the request, stores it, and returns the generated event ID.

## Example: Replay an Event

Configure a destination URL on the webhook endpoint, then send:

```bash
curl -X POST http://127.0.0.1:8000/api/events/<event_id>/replay/
```

RelayScope forwards the captured request to the configured destination and records the delivery result.

## Current Scope and Limitations

This project is an MVP focused on webhook capture, inspection, and replay.

- User authentication and authorization are not implemented.
- Provider-specific webhook signature verification is not implemented.
- Production-grade destination URL validation and SSRF protection are not implemented.
- Replay requests are currently processed synchronously.
- The frontend dashboard and background job processing are not yet implemented.

**Security Note:** Use only trusted destination URLs in this development version. Do not expose real webhook tokens or sensitive payloads publicly.

## License

This project is currently intended as a portfolio project.