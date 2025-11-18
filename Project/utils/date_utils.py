from datetime import datetime, date, timedelta

DATE_FMT = "%Y-%m-%d"

def parse_date(s: str) -> date:
    return datetime.strptime(s, DATE_FMT).date()

def today() -> date:
    return datetime.now().date()

def days_left(deadline_date) -> int:
    if isinstance(deadline_date, str):
        deadline_date = parse_date(deadline_date)
    delta = (deadline_date - today()).days
    return max(delta, 0)
