# reelMarket

**Watch it. Want it. Own it.**

reelMarket is a mobile-first social-commerce prototype: discover products through a creator-style feed, explore seller storefronts, save products, add items to a demo bag, and explore auction-style listings.

## Current prototype
- Responsive Instagram-inspired visual language with original reelMarket branding.
- Product feed with creator stories, seller profiles, likes, saves, follow controls, search, and product detail modals.
- Explore grid, saved shelf, following feed, and auction listings.
- Demo listing creation, shopping bag, and simulated bid flow.
- Accessible labels, reduced-motion support, mobile navigation, and responsive layouts.

## Run it
This is a static HTML prototype. Open `index.html` in a browser, or enable GitHub Pages in repository settings to publish it.

## Important: prototype boundaries
The current interactions run in the browser and use in-memory sample data. User-created listings, follows, likes, and demo bids are not persisted or shared across users. Product imagery is loaded from Unsplash and typography from Google Fonts. The prototype does **not** process payments, upload videos, authenticate users, message sellers, or run real auctions.

Before a public production launch, implement and test:
1. Authentication, seller onboarding, role-based access, and account recovery.
2. Persistent product, media, seller, order, and moderation data.
3. Secure video/image upload with file validation, storage limits, and abuse scanning.
4. Server-authoritative auctions with atomic bid updates, closing rules, anti-sniping policy, and audit logs.
5. Payment gateway integration, refunds, seller payouts, shipping, tax, and dispute workflows.
6. Reporting, content moderation, seller verification, privacy controls, rate limiting, and security monitoring.
7. Automated tests, accessibility checks, performance budgets, and deployment secrets management.

## Suggested next architecture
Keep the initial web client lightweight, then add a typed API and database behind explicit domain boundaries: identity, catalog, media, social interactions, auctions, checkout/orders, and moderation. Never trust client-side prices, seller roles, auction clocks, or bid amounts as authoritative.
