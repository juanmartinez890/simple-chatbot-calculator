from uuid import UUID
from datetime import datetime

class Message:
    def __init__(self, message_id: UUID, request: str, response: str, created_at: datetime):
        self.message_id = message_id
        self.request = request
        self.response = response
        self.created_at = created_at

    def __repr__(self):
        return f"Message({self.message_id}, {self.request}, {self.response}, {self.created_at})"
    
    def to_dict(self):
        return {
            "message_id": str(self.message_id),
            "request": self.request,
            "response": self.response,
            "created_at": self.created_at.isoformat()
        }

