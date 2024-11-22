from http.client import HTTPException
from typing import Dict, List
from uuid import UUID, uuid4
from datetime import datetime, timezone
from models.conversation import Conversation
from models.message import Message
from models.operation import Operation
from schemas.conversation import ConversationMessages
from schemas.message import MessageResponse
import json

from services.llm import LLMService

class ConversationManager:
    def __init__(self):
        self.conversations: Dict[UUID, Conversation] = {}
        self.operations: list[Operation] = []

    def create_conversation_message(self, conversation_id: UUID, request: str)-> MessageResponse:
        # Create conversation if it doesn't already exist
        try:
            conversation = self.conversations[conversation_id]
        except:
            conversation = Conversation(conversation_id=conversation_id, created_at=datetime.now(tz=timezone.utc))
            self.conversations[conversation_id] = conversation
        previous_messages = ", ".join(
            [f"Q{i + 1}: {msg.request}, A{i + 1}: {msg.response}" for i, msg in enumerate(conversation.messages)]
        )
        # Function call to extract operation and result
        llm = LLMService()
        messages = [
            {"role": "system", "content": "System should perform simple calculator operations. Respond, I don't know to anything else not relevant to actions performed as a simple calculator"},
            {"role": "user", "content": request},
        ]
        function_call_response = llm.compose_response(messages, enable_function_calls=True)
        formatted_function_call_response = {}
        try:
            formatted_function_call_response = json.loads(function_call_response)
            self.operations.append(Operation(
                formatted_function_call_response['operation'],
                formatted_function_call_response['result']
            ))
        except json.JSONDecodeError:
            raise HTTPException(
                status_code=500,
                detail="Something went wrong from our end :( )"
            )
        operation_stack = ", ".join(
            [f"Operation {i + 1}: ({operation.operation} = {operation.result})" for i, operation in enumerate(self.operations)]
        )
        # call llm to compose the response
        messages = [
            {"role": "system", "content": 'The system should function as a simple calculator, responding to user queries with the result of basic arithmetic operations. For example, when asked "What is 2 + 2?", the system should respond with "The result is 4." If the user asks to compute based on the previous result, such as "What is the result of adding 5 to the previous result?", the system should use the last computed result and return the appropriate answer, like "The result is 9." If the user asks to reverse the last operation, like "What is the result of subtracting the previous operation?", the system should undo the last operation and provide the new result, for example, "The result is -1." If the query is unrelated to a mathematical operation, such as "What is the weather today?", the system should reply with "I am unable to answer that." This approach ensures the system stays focused on performing arithmetic while gracefully handling irrelevant queries.'},
            {"role": "assistant", "content": f"Previous conversation messages: {previous_messages}"},
            {"role": "assistant", "content": f"Here are the previous conversation messages: {operation_stack}"},
            {"role": "user", "content": request},
        ]
        llm_response = llm.compose_response(messages, enable_function_calls=False)
        # Add new message to conversation
        message = Message(
            message_id=uuid4(),
            request=request,
            response=llm_response, 
            created_at=datetime.now(tz=timezone.utc)
        )
        conversation.add_message(message)
        return message.to_dict()

    def get_all_messages_in_conversation(self, conversation_id: UUID) -> ConversationMessages:
        if conversation_id not in self.conversations:
            raise KeyError(f"Conversation with ID {conversation_id} does not exist.")
        conversation = self.conversations[conversation_id]
        return conversation.to_dict()
    
    def get_all_conversations(self) -> list[ConversationMessages]:
        return list(conversation.to_dict() for conversation in self.conversations.values())

