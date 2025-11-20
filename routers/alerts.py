from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from schemas.alerts import AlertCreate, AlertRead
from crud.alerts import create_alert, list_alerts
from crud.worker import get_active_shift_by_machine, get_worker

router = APIRouter()

@router.post("/alerts", response_model=AlertRead)
def api_create_alert(payload: AlertCreate, db: Session = Depends(get_db)):
    # try to route to worker
    active_shift = get_active_shift_by_machine(db, payload.machine_id)
    if active_shift:
        payload.assigned_worker = active_shift.worker_id
        # try supervisor
        worker = get_worker(db, active_shift.worker_id)
        if worker:
            payload.assigned_supervisor = worker.supervisor_id
    a = create_alert(db, payload)
    return a

@router.get("/alerts")
def api_list_alerts(db: Session = Depends(get_db)):
    return list_alerts(db)
