from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func
from database import Base

class Machine(Base):
    __tablename__ = "machines"
    id = Column(Integer, primary_key=True, index=True)
    machine_code = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    location = Column(String, nullable=True)
    status = Column(String, default="UNKNOWN")
    last_active = Column(DateTime(timezone=True), nullable=True)

class MachineReading(Base):
    __tablename__ = "machine_readings"
    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(Integer, ForeignKey("machines.id"), index=True, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    temperature = Column(Float, nullable=False)
    vibration = Column(Float, nullable=False)
    load = Column(Float, nullable=False)
    pressure = Column(Float, nullable=True)
    stability = Column(Float, nullable=True)
