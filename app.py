```python
import streamlit as st
import ollama
import json
import re
from pathlib import Path

# Page Configuration
st.set_page_config(
    page_title="MemoraAI",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 MemoraAI")
st.caption("Your Personal AI Memory Assistant")

# Memory File
MEMORY_FILE = Path("memora_memory.json")

# Load Memory Data
def load_data():
    if MEMORY_FILE.exists():
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)

    return {
        "memories": [],
        "chat_history": []
    }

# Save Memory Data
def save_data(data):
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)

data = load_data()

# Memory Retrieval
def retrieve_memory(question, memories):
    question_words = set(
        re.findall(r"\w+", question.lower())
    )

    results = []

    for memory in memories:
        memory_words = set(
            re.findall(r"\w+", memory.lower())
        )

        common_words = question_words.intersection(memory_words)

        if len(common_words) > 0:
            results.append(memory)

    return results[:5]

# Generate AI Response
def generate_response(question, history, memories):

    relevant_memories = retrieve_memory(
        question, memories
    )

    memory_context = "\n".join(relevant_memories)

    system_prompt = f"""
    You are MemoraAI, a helpful personal AI assistant.

    Use the following saved memories when relevant:

    {memory_context}

    Do not invent personal information.
    If the answer is not available in memory,
    honestly say that you do not know.
    """

    messages = [
        {"role": "system", "content": system_prompt}
    ]

    messages.extend(history[-10:])

    messages.append({
        "role": "user",
        "content": question
    })

    response = ollama.chat(
        model="llama3.2",
        messages=messages
    )

    return response["message"]["content"], relevant_memories


# Sidebar - Memory Vault
st.sidebar.header("💾 Memory Vault")

new_memory = st.sidebar.text_area(
    "Add a new memory"
)

if st.sidebar.button("Save Memory"):

    if new_memory.strip():
        data["memories"].append(new_memory.strip())
        save_data(data)
        st.sidebar.success("Memory saved!")
        st.rerun()

    else:
        st.sidebar.warning("Enter a memory first.")

# Display Saved Memories
st.sidebar.subheader("Saved Memories")

for index, memory in enumerate(data["memories"]):

    st.sidebar.write(memory)

    if st.sidebar.button(
        "Delete",
        key=f"delete_{index}"
    ):
        data["memories"].pop(index)
        save_data(data)
        st.rerun()

# Clear Chat History
if st.sidebar.button("Clear Chat History"):
    data["chat_history"] = []
    save_data(data)
    st.rerun()

# Display Chat History
for message in data["chat_history"]:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# User Chat Input
question = st.chat_input(
    "Ask something..."
)

if question:

    with st.chat_message("user"):
        st.write(question)

    try:

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                answer, used_memories = generate_response(
                    question,
                    data["chat_history"],
                    data["memories"]
                )

            st.write(answer)

            if used_memories:
                with st.expander("Memories used"):
                    for memory in used_memories:
                        st.write("- " + memory)

        data["chat_history"].append({
            "role": "user",
            "content": question
        })

        data["chat_history"].append({
            "role": "assistant",
            "content": answer
        })

        save_data(data)

    except Exception as error:

        st.error(
            "Unable to connect to Ollama. "
            "Please check whether Ollama is running "
            "and the Llama 3.2 model is installed."
        )

        st.caption(str(error))
```