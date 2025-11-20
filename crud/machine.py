from sqlalchemy.orm import Session
from models.machine import Machine, MachineReading
from utils.stability import compute_stability
from datetime import datetime

def get_machine(db: Session, machine_id: int):
    return db.query(Machine).filter(Machine.id == machine_id).first()

def get_machine_by_code(db: Session, code: str):
    return db.query(Machine).filter(Machine.machine_code == code).first()

def create_machine(db: Session, machine_in):
    m = Machine(machine_code=machine_in.machine_code, name=machine_in.name, location=machine_in.location)
    db.add(m); db.commit(); db.refresh(m)
    return m

def add_reading(db: Session, machine_id: int, reading_in):
    stability = compute_stability(reading_in.temperature, reading_in.vibration, reading_in.load)
    mr = MachineReading(
        machine_id=machine_id,
        timestamp=reading_in.timestamp or datetime.utcnow(),
        temperature=reading_in.temperature,
        vibration=reading_in.vibration,
        load=reading_in.load,
        pressure=reading_in.pressure,
        stability=stability
    )
    db.add(mr)
    # update machine last_active/status
    machine = get_machine(db, machine_id)
    if machine:
        machine.last_active = mr.timestamp
        machine.status = "RUNNING"
    db.commit()
    db.refresh(mr)
    return mr

def get_latest_readings(db: Session, machine_id: int=None, limit: int=100):
    q = db.query(MachineReading)
    if machine_id:
        q = q.filter(MachineReading.machine_id == machine_id)
    return q.order_by(MachineReading.timestamp.desc()).limit(limit).all()

def get_history(db: Session, machine_id: int, start=None, end=None, limit=1000):
    q = db.query(MachineReading).filter(MachineReading.machine_id == machine_id)
    if start:
        q = q.filter(MachineReading.timestamp >= start)
    if end:
        q = q.filter(MachineReading.timestamp <= end)
    return q.order_by(MachineReading.timestamp.asc()).limit(limit).all()
