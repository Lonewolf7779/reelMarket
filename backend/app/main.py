from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.config import settings
from app.database import Base, engine, get_db
from app.models import Product
from app.schemas import ProductCreate, ProductRead


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title=settings.app_name, version="0.1.0", lifespan=lifespan)


@app.get("/api/v1/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok", "service": "reelMarket API"}


@app.post("/api/v1/products", response_model=ProductRead, status_code=status.HTTP_201_CREATED, tags=["catalog"])
def create_product(payload: ProductCreate, db: Session = Depends(get_db)) -> Product:
    product = Product(**payload.model_dump(mode="json"))
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


@app.get("/api/v1/products", response_model=list[ProductRead], tags=["catalog"])
def list_products(
    q: str | None = Query(default=None, max_length=120),
    category: str | None = Query(default=None, max_length=60),
    limit: int = Query(default=24, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
) -> list[Product]:
    statement = select(Product).order_by(Product.created_at.desc(), Product.id.desc())
    if q and q.strip():
        term = f"%{q.strip()}%"
        statement = statement.where(Product.title.ilike(term) | Product.description.ilike(term) | Product.seller_name.ilike(term))
    if category and category.strip():
        statement = statement.where(Product.category.ilike(category.strip()))
    return list(db.scalars(statement.offset(offset).limit(limit)).all())


@app.get("/api/v1/products/{product_id}", response_model=ProductRead, tags=["catalog"])
def get_product(product_id: int, db: Session = Depends(get_db)) -> Product:
    product = db.get(Product, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
