# AI Chatbot with ChatterBot

## Overview
This AI chatbot is built using the ChatterBot library and trained on a set of domain-specific customer support questions related to bridal gown orders. It supports both general and custom conversational knowledge and can be interacted with in real time.

## Features
- Trained on domain-specific questions from a JSON dataset
- Memory persistence using SQLite database
- Customizable and extendable logic adapters
- Modular structure with training, testing, and runtime components

## Technologies Used
- Python 3.8–3.9
- ChatterBot
- Natural Language Processing (NLP)
- SQLite

## Setup Instructions

### 1. Create a virtual environment (recommended)
```bash
python -m venv chatbot-env
source chatbot-env/bin/activate  # Windows: chatbot-env\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the chatbot
This script trains the bot using `data_sample_specific.json`.

```bash
python train_chatbot_domain_only.py
```

This will create a SQLite database file `my_chatbot_db.sqlite3` for persistent memory.

### 4. Run the chatbot
```bash
python chatbot_app.py
```

### 5. Run test script (optional)
```bash
python test_chat.py
```

## Sample Training Data

The custom training data is in `data_sample_specific.json`:
```json
{
  "question": "How do I return a product?",
  "answer": "To return a product, please contact our support team with your order number..."
}
```

## File Descriptions

| File | Purpose |
|------|---------|
| `chatbot_app.py` | Runs the chatbot with memory |
| `train_chatbot_domain_only.py` | Trains the bot using domain-specific Q&A |
| `data_sample_specific.json` | Custom training corpus |
| `test_chat.py` | Script to simulate sample user queries |
| `my_chatbot_db.sqlite3` | Persistent database (excluded from GitHub) |

## Notes
- The ChatterBot library may not work with Python 3.10+; Python 3.8 or 3.9 is recommended.
- For deployment, consider integrating with a web UI using Flask or Streamlit.

## License
MIT License

---

