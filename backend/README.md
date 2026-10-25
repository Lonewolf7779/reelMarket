# reelMarket API

The first backend milestone establishes a persistent catalog API. This is a development foundation, not a production marketplace yet.

## Run locally

```bash
cd backend
python -m venv .venv
# Activate the environment, then:
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for the interactive API documentation.

## Endpoints

- `GET /api/v1/health`: health check
- `POST /api/v1/products`: create a product listing
- `GET /api/v1/products`: list, search, and filter listings (`q`, `category`, `limit`, `offset`)
- `GET /api/v1/products/{product_id}`: retrieve a listing

Prices are integer minor units. For INR, `49900` means ₹499.00. Do not accept client-calculated totals as authoritative during checkout.

## Current limitations

- SQLite is configured for local development; production should use managed PostgreSQL and migrations.
- No authentication/authorization yet. Do not expose listing creation publicly until identity, seller ownership, and rate limits are implemented.
- Media URLs are metadata only. Secure upload/storage, moderation, payment processing, orders, and server-authoritative auctions are not implemented.
- Before production, add Alembic migrations, structured logging, security headers, CORS allowlists, request limits, secrets management, and integration tests against the production database.
