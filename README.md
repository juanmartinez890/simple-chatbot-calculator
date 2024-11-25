# AI-Powered Chat Conversation API

This repository contains a **RESTful API** for real-time chat conversations with an AI agent specialized in solving basic math problems. The API allows managing multiple chat sessions, sending and retrieving messages, and providing accurate answers to math queries.

## Features

- **Start a new conversation**:  
  Create independent chat sessions with the AI.  
  ```http
  POST /conversations
  ```

- **Send messages in a conversation**:  
  Interact with the AI and receive immediate responses.  
  ```http
  POST /conversations/{conversation_id}/messages
  ```

- **Retrieve all conversations**:  
  Get a list of all active or past conversations and their details.  
  ```http
  GET /conversations
  ```

- **Retrieve all messages in a conversation**:  
  Access the history of messages exchanged within a specific conversation.  
  ```http
  GET /conversations/{conversation_id}/messages
  ```

---

## Example Interaction

```plaintext
User: Hi, can you help with some math?
Agent: Absolutely! What do you need assistance with?
User: What’s 45 plus 78?
Agent: That’s 123. Anything else?
User: Multiply it by 2.
Agent: The result is 246. Let me know if there’s more I can help with!
```

---

## Getting Started

### Prerequisites

- Python 3.9+
- `pip` for managing dependencies

### Clone the Repository

```bash
git clone https://github.com/your-username/ai-chat-conversation-api.git
cd ai-chat-conversation-api
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Server

```bash
uvicorn app:app --reload
```

### Access API Documentation

Visit `http://127.0.0.1:8000/docs` to interact with the API.

---

## Project Structure

```
├── app/
│   ├── main.py            # Entry point for the API
│   ├── models/            # Data models and schemas
│   ├── services/          # Business logic and helpers
│   ├── routes/            # API endpoints
│   └── tests/             # Unit and integration tests
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Ignored files and folders
```

---

## Future Enhancements

- 🛠️ **Persistent Storage**: Add support for storing conversations in a database.  
- 🚀 **Expanded AI Capabilities**: Support more complex queries and contextual understanding.  
- 🔒 **User Authentication**: Implement user and session management.  
- 💡 **Advanced Features**: Introduce context switching and richer conversational workflows.  

---

## Contributing

Contributions are welcome! Please follow these steps:  

1. Fork the repository.  
2. Create a new branch:  
   ```bash
   git checkout -b feature/your-feature-name
   ```  
3. Commit your changes and push the branch:  
   ```bash
   git push origin feature/your-feature-name
   ```  
4. Open a pull request and describe your changes.  

---

## License

This project is licensed under the [MIT License](LICENSE).  

---

Feel free to star ⭐ the repository if you find it helpful!
