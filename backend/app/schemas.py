from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class ProductCreate(BaseModel):
    title: str = Field(min_length=2, max_length=120)
    description: str = Field(default="", max_length=4000)
    price_paise: int = Field(gt=0, le=100_000_000)
    currency: str = Field(default="INR", min_length=3, max_length=3, pattern="^[A-Z]{3}$")
    seller_name: str = Field(min_length=2, max_length=80)
    category: str = Field(min_length=2, max_length=60)
    media_url: HttpUrl | None = None


class ProductRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    description: str
    price_paise: int
    currency: str
    seller_name: str
    category: str
    media_url: str | None
    created_at: datetime
