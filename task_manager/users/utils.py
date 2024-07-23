import json
from pathlib import Path


def load_data(path):
    with open(Path(f'task_manager/users/fixtures/{path}')) as file:
        return json.loads(file.read())