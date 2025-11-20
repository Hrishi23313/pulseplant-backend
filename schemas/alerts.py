from pydantic import BaseModel
from typing import Optional

class AlertCreate(BaseModel):
    machine_id: int
    alert_type: str
    severity: str
    message: Optional[str] = None

class AlertRead(BaseModel):
    id: int
    machine_id: int
    alert_type: str
    severity: str
    message: Optional[str]

    class Config:
        orm_mode = True
