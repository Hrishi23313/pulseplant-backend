from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, ForeignKey, func
from database import Base

class Worker(Base):
    __tablename__ = "workers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    badge_id = Column(String, nullable=True, unique=True)
    role = Column(String, default="operator")
    supervisor_id = Column(Integer, nullable=True)

class Shift(Base):
    __tablename__ = "shifts"
    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(Integer, ForeignKey("workers.id"), index=True, nullable=False)
    machine_id = Column(Integer, index=True, nullable=True)
    start_time = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    end_time = Column(DateTime(timezone=True), nullable=True, index=True)
    auto_closed = Column(Boolean, default=False)
    hours = Column(Float, nullable=True)
    status = Column(String, default="active")
