import json
from task import Task

class Storage:
    def __init__(self, filename='tasks.json'):
        self.filename = filename

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                tasks_data = json.load(file)
                return [Task.from_dict(task) for task in tasks_data]
        except FileNotFoundError:
            return []

    def save_tasks(self, tasks):
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in tasks], file)
