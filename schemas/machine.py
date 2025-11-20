from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class MachineCreate(BaseModel):
    machine_code: str
    name: str
    location: Optional[str] = None

class MachineRead(BaseModel):
    id: int
    machine_code: str
    name: str
    location: Optional[str]
    status: Optional[str]
    last_active: Optional[datetime]

    class Config:
        orm_mode = True

class MachineReadingCreate(BaseModel):
    timestamp: Optional[datetime] = None
    temperature: float
    vibration: float
    load: float
    pressure: Optional[float] = None

class MachineReadingRead(BaseModel):
    id: int
    machine_id: int
    timestamp: Optional[datetime]
    temperature: float
    vibration: float
    load: float
    pressure: Optional[float]
    stability: Optional[float]

    class Config:
        orm_mode = True
