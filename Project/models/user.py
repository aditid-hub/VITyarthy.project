import hashlib
from utils.file_handler import read_json, write_json

USERS_FILE = "users.json"

def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def create_user(username: str, password: str) -> bool:
    users = read_json(USERS_FILE, default={})
    if username in users:
        return False
    users[username] = {"password_hash": _hash_password(password)}
    write_json(USERS_FILE, users)
    return True

def verify_user(username: str, password: str) -> bool:
    users = read_json(USERS_FILE, default={})
    if username not in users:
        return False
    return users[username]["password_hash"] == _hash_password(password)
