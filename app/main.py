from fastapi import FastAPI

from app.core.config import settings
from app.core.database import Base, engine

from app.api.routes import auth as auth_routes


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME
)

app.include_router(auth_routes.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
