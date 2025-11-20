from datetime import datetime, timedelta

DOWNTIME_GAP_SECONDS = 90

def is_machine_down(last_timestamp: datetime, now: datetime) -> bool:
    return (now - last_timestamp).total_seconds() > DOWNTIME_GAP_SECONDS
