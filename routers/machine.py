from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from schemas.machine import MachineCreate, MachineRead, MachineReadingCreate, MachineReadingRead
from crud.machine import create_machine, get_machine_by_code, get_machine, add_reading, get_latest_readings, get_history

router = APIRouter()

@router.post("/machines", response_model=MachineRead)
def api_create_machine(payload: MachineCreate, db: Session = Depends(get_db)):
    existing = get_machine_by_code(db, payload.machine_code)
    if existing:
        raise HTTPException(status_code=400, detail="Machine code already exists")
    m = create_machine(db, payload)
    return m

@router.post("/machines/{machine_id}/readings", response_model=MachineReadingRead)
def api_add_reading(machine_id: int, payload: MachineReadingCreate, db: Session = Depends(get_db)):
    m = get_machine(db, machine_id)
    if not m:
        raise HTTPException(status_code=404, detail="Machine not found")
    mr = add_reading(db, machine_id, payload)
    return mr

@router.get("/machines/{machine_id}/history")
def api_history(machine_id: int, db: Session = Depends(get_db)):
    m = get_machine(db, machine_id)
    if not m:
        raise HTTPException(status_code=404, detail="Machine not found")
    rows = get_history(db, machine_id)
    return rows

@router.get("/machines/latest")
def api_latest(db: Session = Depends(get_db)):
    rows = get_latest_readings(db)
    return rows
