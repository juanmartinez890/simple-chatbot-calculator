from uuid import UUID
from datetime import datetime
from typing import List
from models.message import Message

class Conversation:
    def __init__(self, conversation_id: UUID, created_at: datetime):
        self.conversation_id = conversation_id
        self.created_at = created_at
        self.messages: List[Message] = []

    def add_message(self, message: Message):
        self.messages.append(message)

    def __repr__(self):
        return f"Conversation({self.conversation_id}, {self.created_at}, Messages={len(self.messages)})"
    
    def to_dict(self):
        return {
            "conversation_id": str(self.conversation_id),
            "created_at": self.created_at.isoformat(), 
            "messages": [message.to_dict() for message in self.messages]
        }