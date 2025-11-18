from utils.date_utils import days_left, today
from math import isclose

def calculate_load_factor(difficulty: int, hours_required: float, deadline_str: str) -> float:
    d_left = days_left(deadline_str)
    if d_left == 0:
        # extremely urgent: treat as hours * difficulty (no days to spread)
        return difficulty * hours_required
    return (difficulty * hours_required) / d_left

def classify_load(lf: float) -> str:
    if lf < 1:
        return "Low"
    if 1 <= lf < 2:
        return "Moderate"
    if 2 <= lf < 3:
        return "High"
    return "Overload"

def detect_overloaded_tasks(tasks):
    # tasks: list of dicts with difficulty,hours_required,deadline
    overloaded = []
    for t in tasks:
        lf = calculate_load_factor(t["difficulty"], t["hours_required"], t["deadline"])
        if lf >= 3:
            overloaded.append((t, lf))
    return overloaded
