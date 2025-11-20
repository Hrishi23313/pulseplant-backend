from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from database import Base

class MachineAlert(Base):
    __tablename__ = "machine_alerts"
    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(Integer, ForeignKey("machines.id"), index=True, nullable=False)
    alert_type = Column(String, nullable=False)
    severity = Column(String, nullable=False)
    message = Column(String, nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    assigned_worker = Column(Integer, nullable=True)
    assigned_supervisor = Column(Integer, nullable=True)
