import uuid
from dataclasses import dataclass, asdict
from typing import Dict, Any
from utils.file_handler import read_json, write_json

TASKS_FILE = "tasks.json"


# OPTIONAL Task class (not used directly by app, but kept for structure)
@dataclass
class Task:
    id: str
    name: str
    course: str
    task_type: str
    difficulty: int
    hours_required: float
    deadline: str
    priority: int
    owner: str

    def as_dict(self):
        return asdict(self)


# ---------------------------
# LOAD ALL TASKS FOR USER
# ---------------------------
def load_tasks(username: str):
    all_tasks = read_json(TASKS_FILE, default=[])
    return [t for t in all_tasks if t.get("owner") == username]


# ---------------------------
# SAVE TASK (dict supported)
# ---------------------------
def save_task(task_data: dict):
    """Save or update task. Accepts dict, not Task object."""
    all_tasks = read_json(TASKS_FILE, default=[])

    # If incoming dict has id → update
    updated = False
    for i, t in enumerate(all_tasks):
        if t["id"] == task_data["id"]:
            all_tasks[i] = task_data
            updated = True
            break

    # Otherwise add new
    if not updated:
        all_tasks.append(task_data)

    write_json(TASKS_FILE, all_tasks)


# ---------------------------
# DELETE TASK
# ---------------------------
def delete_task(task_id: str):
    all_tasks = read_json(TASKS_FILE, default=[])
    all_tasks = [t for t in all_tasks if t["id"] != task_id]
    write_json(TASKS_FILE, all_tasks)


# ---------------------------
# CREATE NEW TASK DICT
# ---------------------------
def new_task_dict(name, course, task_type, difficulty, hours_required, deadline, priority, owner):
    return {
        "id": str(uuid.uuid4()),
        "name": name,
        "course": course,
        "task_type": task_type,
        "difficulty": int(difficulty),
        "hours_required": float(hours_required),
        "deadline": deadline,
        "priority": int(priority),
        "owner": owner
    }
