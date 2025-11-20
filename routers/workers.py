from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from schemas.worker import WorkerCreate, WorkerRead
from crud.worker import create_worker, get_worker, list_workers

router = APIRouter()

@router.post("/workers", response_model=WorkerRead)
def api_create_worker(payload: WorkerCreate, db: Session = Depends(get_db)):
    w = create_worker(db, payload)
    return w

@router.get("/workers/{worker_id}", response_model=WorkerRead)
def api_get_worker(worker_id: int, db: Session = Depends(get_db)):
    w = get_worker(db, worker_id)
    if not w:
        raise HTTPException(status_code=404, detail="Worker not found")
    return w

@router.get("/workers")
def api_list_workers(db: Session = Depends(get_db)):
    return list_workers(db)
