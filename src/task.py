from datetime import datetime


class Task:
    def __init__(self, title, description, completed=False, created_at=None, completed_at=None):
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at or datetime.now().isoformat()
        self.completed_at = completed_at

    def mark_completed(self):
        self.completed = True
        self.completed_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at,
            'completed_at': self.completed_at
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data.get('title', ''),
            description=data.get('description', ''),
            completed=data.get('completed', False),
            created_at=data.get('created_at', datetime.now().isoformat()),
            completed_at=data.get('completed_at')
        )
