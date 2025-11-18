from core.load_engine import calculate_load_factor
from utils.date_utils import days_left, today
from datetime import timedelta, date

def generate_daily_plan(tasks, daily_available_hours=4, days_span=14):

    meta = []
    for t in tasks:
        lf = calculate_load_factor(t["difficulty"], t["hours_required"], t["deadline"])
        dl = days_left(t["deadline"])

        meta.append({
            **t,
            "load_factor": lf,
            "days_left": dl,
            "hours_remaining": t["hours_required"],
        })

    # Sort by urgency + priority
    meta.sort(key=lambda x: (-x["load_factor"], x["priority"], x["days_left"]))

    plan = {}
    start = today()

    # Build date calendar
    for i in range(days_span):
        d = start + timedelta(days=i)
        plan[d.isoformat()] = {
            "date": d.isoformat(),
            "slots": [],
            "available_hours": daily_available_hours
        }

    # Allocate tasks
    for t in meta:
        deadline = date.fromisoformat(t["deadline"])

        if deadline < start:
            target_days = [start]
        else:
            last_day = min(deadline, start + timedelta(days=days_span - 1))
            target_days = [start + timedelta(days=i) for i in range((last_day - start).days + 1)]

        while t["hours_remaining"] > 0 and target_days:
            allocated = False

            for d in target_days:
                key = d.isoformat()

                if plan[key]["available_hours"] <= 0:
                    continue

                chunk = min(0.5, t["hours_remaining"], plan[key]["available_hours"])
                if chunk <= 0:
                    continue

                plan[key]["slots"].append({
                    "task_id": t["id"],
                    "task_name": t["name"],
                    "course": t["course"],
                    "hours": chunk
                })

                plan[key]["available_hours"] = round(plan[key]["available_hours"] - chunk, 2)
                t["hours_remaining"] = round(t["hours_remaining"] - chunk, 2)

                allocated = True
                break

            if not allocated:
                break

    return [plan[d] for d in sorted(plan.keys())]
