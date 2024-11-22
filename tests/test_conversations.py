from fastapi.testclient import TestClient
from uuid import uuid4
from main import app  # Import the FastAPI app

client = TestClient(app)

def test_create_new_conversation_message():
    """
    Test adding a new message to a conversation.
    """
    conversation_id = str(uuid4())  # Generate a unique conversation ID
    payload = {"request": "What is 2 + 2?"}

    response = client.post(f"/api/v1/conversations/{conversation_id}/messages", json=payload)

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["request"] == "What is 2 + 2?"
    assert "response" in response_data
    assert "message_id" in response_data
    assert "created_at" in response_data


def test_get_all_conversations():
    """
    Test retrieving all conversations.
    """
    # First, create some conversations
    for _ in range(3):
        conversation_id = str(uuid4())
        payload = {"request": "What is 5 * 5?"}
        client.post(f"/api/v1/conversations/{conversation_id}/messages", json=payload)

    # Now retrieve all conversations
    response = client.get("/api/v1/conversations/")
    assert response.status_code == 200

    conversations = response.json()
    assert isinstance(conversations, list)
    assert len(conversations) > 0  # Ensure at least one conversation exists
    for conversation in conversations:
        assert "conversation_id" in conversation
        assert "created_at" in conversation
        assert "messages" in conversation

        
def test_get_conversation_messages():
    """
    Test retrieving all messages from a specific conversation.
    """
    conversation_id = str(uuid4())
    payload = {"request": "What is 10 - 3?"}

    # Add a message to the conversation
    client.post(f"/api/v1/conversations/{conversation_id}/messages", json=payload)

    # Retrieve messages from the conversation
    response = client.get(f"/api/v1/conversations/{conversation_id}/messages")
    assert response.status_code == 200

    conversation_data = response.json()
    assert "conversation_id" in conversation_data
    assert conversation_data["conversation_id"] == conversation_id
    assert "messages" in conversation_data
    assert len(conversation_data["messages"]) > 0
    assert conversation_data["messages"][0]["request"] == "What is 10 - 3?"


def test_get_conversation_not_found():
    """
    Test retrieving messages for a non-existent conversation.
    """
    invalid_conversation_id = str(uuid4())

    response = client.get(f"/api/v1/conversations/{invalid_conversation_id}/messages")
    assert response.status_code == 404
    assert response.json()["detail"] == f"Conversation with ID {invalid_conversation_id} does not exist."
