import os
from pathlib import Path
from fastapi.testclient import TestClient

# Use an isolated database for this test module before importing the app.
test_db = Path(__file__).with_name("test_reelmarket.db")
os.environ["DATABASE_URL"] = f"sqlite:///{test_db}"

from app.main import app  # noqa: E402
from app.database import Base, engine  # noqa: E402


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
client = TestClient(app)


def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_and_search_product():
    payload = {
        "title": "Canvas Tote Bag",
        "description": "Everyday cotton tote",
        "price_paise": 49900,
        "seller_name": "North Studio",
        "category": "Accessories",
    }
    created = client.post("/api/v1/products", json=payload)
    assert created.status_code == 201
    assert created.json()["price_paise"] == 49900
    product_id = created.json()["id"]

    found = client.get("/api/v1/products", params={"q": "Canvas"})
    assert found.status_code == 200
    assert any(item["id"] == product_id for item in found.json())

    detail = client.get(f"/api/v1/products/{product_id}")
    assert detail.status_code == 200
    assert detail.json()["title"] == "Canvas Tote Bag"


def test_reject_invalid_price():
    response = client.post("/api/v1/products", json={
        "title": "Bad price", "price_paise": 0, "seller_name": "Seller", "category": "Other"
    })
    assert response.status_code == 422
