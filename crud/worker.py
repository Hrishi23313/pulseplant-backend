from sqlalchemy.orm import Session
from models.worker import Worker, Shift
from datetime import datetime

def create_worker(db: Session, worker_in):
    w = Worker(name=worker_in.name, badge_id=worker_in.badge_id, role=worker_in.role, supervisor_id=worker_in.supervisor_id)
    db.add(w); db.commit(); db.refresh(w)
    return w

def get_worker(db: Session, worker_id: int):
    return db.query(Worker).filter(Worker.id == worker_id).first()

def list_workers(db: Session, limit: int=100):
    return db.query(Worker).limit(limit).all()

def start_shift(db: Session, worker_id: int, machine_id: int=None):
    # ensure no active shift for this worker
    existing = db.query(Shift).filter(Shift.worker_id==worker_id, Shift.end_time==None).first()
    if existing:
        return None
    s = Shift(worker_id=worker_id, machine_id=machine_id)
    db.add(s); db.commit(); db.refresh(s)
    return s

def end_shift(db: Session, shift_id: int, end_time=None):
    s = db.query(Shift).filter(Shift.id == shift_id).first()
    if not s or s.end_time:
        return None
    s.end_time = end_time or datetime.utcnow()
    s.hours = (s.end_time - s.start_time).total_seconds()/3600.0
    s.status = "ended"
    db.commit(); db.refresh(s)
    return s

def get_active_shift_by_worker(db: Session, worker_id: int):
    return db.query(Shift).filter(Shift.worker_id==worker_id, Shift.end_time==None).first()

def get_active_shift_by_machine(db: Session, machine_id: int):
    return db.query(Shift).filter(Shift.machine_id==machine_id, Shift.end_time==None).first()
