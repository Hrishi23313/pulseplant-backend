from fastapi import FastAPI
from database import engine, Base
from routers import machine, workers, shifts, health

app = FastAPI(title="PulsePlant API - Starter")

# create tables
Base.metadata.create_all(bind=engine)

app.include_router(machine.router, prefix="/api", tags=["machines"])
app.include_router(workers.router, prefix="/api", tags=["workers"])
app.include_router(shifts.router, prefix="/api", tags=["shifts"])
app.include_router(health.router, prefix="/api", tags=["health"])
