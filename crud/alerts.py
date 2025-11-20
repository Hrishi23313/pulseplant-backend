from sqlalchemy.orm import Session
from models.alerts import MachineAlert

def create_alert(db: Session, alert_in):
    a = MachineAlert(
        machine_id=alert_in.machine_id,
        alert_type=alert_in.alert_type,
        severity=alert_in.severity,
        message=alert_in.message
    )
    db.add(a); db.commit(); db.refresh(a)
    return a

def list_alerts(db: Session, limit:int=100):
    return db.query(MachineAlert).order_by(MachineAlert.timestamp.desc()).limit(limit).all()
