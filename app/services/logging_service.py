from datetime import datetime


def log_agent_event(agent_name: str, message: str):
    timestamp = datetime.now().isoformat()
    print(f"[{timestamp}] [{agent_name}] {message}")
    