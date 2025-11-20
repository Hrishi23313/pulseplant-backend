from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from schemas.worker import ShiftCreate, ShiftEnd, ShiftRead
from crud.worker import start_shift, end_shift, get_active_shift_by_worker, get_active_shift_by_machine

router = APIRouter()

@router.post("/shift/start", response_model=ShiftRead)
def api_start_shift(payload: ShiftCreate, db: Session = Depends(get_db)):
    # check worker
    active = get_active_shift_by_worker(db, payload.worker_id)
    if active:
        raise HTTPException(status_code=400, detail="Worker already has active shift")
    s = start_shift(db, payload.worker_id, payload.machine_id)
    return s

@router.post("/shift/end", response_model=ShiftRead)
def api_end_shift(payload: ShiftEnd, db: Session = Depends(get_db)):
    s = end_shift(db, payload.shift_id, payload.end_time)
    if not s:
        raise HTTPException(status_code=400, detail="Shift not found or already ended")
    return s

@router.get("/shift/current")
def api_current_shift(worker_id: int = None, machine_id: int = None, db: Session = Depends(get_db)):
    if worker_id:
        s = get_active_shift_by_worker(db, worker_id)
        return s
    if machine_id:
        s = get_active_shift_by_machine(db, machine_id)
        return s
    raise HTTPException(status_code=400, detail="provide worker_id or machine_id")
