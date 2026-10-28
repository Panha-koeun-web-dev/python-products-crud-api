
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import Base, engine
from app.models import Product
from app.routers.products import router as products_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Products CRUD API",
    description="Products CRUD API with PostgreSQL",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(products_router)

@app.get("/")
def home():
    return {"message": "Products API is running"}


