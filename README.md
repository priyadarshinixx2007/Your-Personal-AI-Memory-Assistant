# MemoraAI – Your Personal AI Memory Assistant

> A chatbot that remembers your conversations.

MemoraAI is a local AI-powered memory chatbot developed using Python, Streamlit, and Ollama. It allows users to store personal information, retrieve relevant memories, and interact with an AI chatbot using a locally running Large Language Model (LLM).

Unlike traditional chatbots that do not retain personal information between sessions, MemoraAI maintains a local memory vault that stores user-provided information and retrieves relevant details during conversations.

## Features

- Local memory storage using JSON
- AI-powered conversations using Ollama
- Memory retrieval using keyword matching
- Add and delete individual memories
- Persistent memory storage
- Chat history management
- Local-first architecture
- Simple and interactive Streamlit interface
- Integration with locally running LLM models

## Project Structure

```text
MemoraAI/
│
├── app.py
├── requirements.txt
├── README.md
└── memora_memory.json
```

## Technologies Used

- Python
- Streamlit
- Ollama
- JSON
- Llama 3.2

## Requirements

- Python 3.10 or later
- Ollama installed on your system
- Internet connection for initial package and model downloads
- A locally downloaded Ollama model

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd MemoraAI
```

### 3. Create a Virtual Environment

```bash
python3 -m venv venv
```

Activate the virtual environment:

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Install and Download the Ollama Model

Install Ollama from:

https://ollama.com/

Download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

## How It Works

1. **Memory Storage:** Users can add personal information to the local memory vault.
2. **Memory Retrieval:** The application searches stored memories for relevant keywords based on the user's message.
3. **AI Conversation:** Relevant memories are provided as context to the Ollama language model.
4. **Response Generation:** The AI generates responses using the user's question and retrieved information.
5. **Persistent Storage:** Memories and chat history are stored locally in a JSON file.

## Privacy

MemoraAI follows a local-first approach. User memories and chat history are stored on the local system. AI responses are generated through a locally running Ollama model without requiring a hosted AI API.

## Future Improvements

- Semantic memory retrieval using vector embeddings
- Automatic memory extraction from conversations
- Memory categorization and organization
- Multiple chat sessions
- Advanced memory search
- Memory import and export

## Author

Developed as a Large Language Model (LLM) project using Python, Streamlit, and Ollama.