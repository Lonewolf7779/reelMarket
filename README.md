# reelMarket

**Watch it. Want it. Own it.**

reelMarket is being developed as a mobile-first social-commerce marketplace where people discover products through short videos, shop from sellers, and eventually bid in real auctions.

## Repository status

This repository currently contains two distinct pieces:

- **Frontend prototype:** `index.html`, a static UI prototype with sample feed data and simulated interactions.
- **Backend foundation:** `backend/`, a FastAPI application with a persistent SQLAlchemy product catalog API, validation schemas, Dockerfile, environment example, and API tests.

Neither piece should be described as a production-ready marketplace yet.

## Backend quick start

```bash
cd backend
python -m venv .venv
# Activate the virtual environment
pip install -r requirements.txt
uvicorn app.main:app --reload
```

- API health: `http://127.0.0.1:8000/api/v1/health`
- Interactive API docs: `http://127.0.0.1:8000/docs`
- Product API details and limitations: [backend/README.md](backend/README.md)

## Current backend API

- `GET /api/v1/health`
- `POST /api/v1/products`
- `GET /api/v1/products?q=...&category=...`
- `GET /api/v1/products/{product_id}`

Product records are stored in SQLite for local development. Prices are integer minor units, so `49900` represents ₹499.00.

## Not implemented yet

- Authentication, sessions, seller ownership, and account recovery
- Real image/video uploads and media storage
- Likes, follows, comments, messaging, and notifications persisted across accounts
- Cart checkout, orders, payments, refunds, shipping, and payouts
- Server-authoritative auctions and anti-sniping rules
- Moderation, seller verification, abuse reporting, and production monitoring
- Production database migrations, deployment configuration, and security hardening

The frontend's likes, follows, bag, listing creation, and bids remain demo-only. Do not use it for real transactions.

## Build roadmap

1. Catalog API and automated tests
2. Identity, users, and seller permissions
3. Media upload/storage and real video feed
4. Social interactions and product discovery
5. Cart, orders, and payment-provider integration
6. Atomic auction engine with audit trail
7. Moderation, security review, and production deployment

A GitHub Pages deployment is separate from the backend deployment. The Pages workflow needs the repository's Pages source configured to GitHub Actions.
