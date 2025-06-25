import os
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import nltk



# Update to the correct path for your domain-specific data only:
DOMAIN_JSON_FILE = "/Volumes/Seagate/CSC525/Mod8/CahtbotSubmission/data_sample_specific.json"


DATABASE_URI = "sqlite:///my_chatbot_db.sqlite3"

# Initialize the chatbot
chatbot = ChatBot(
    "DomainChatBot",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    database_uri=DATABASE_URI
)

# Create the trainer
trainer = ListTrainer(chatbot)

def load_conversation_pairs_from_json(json_path):
    """
    Loads conversation pairs from a single .json file:
      [ {"question":"...", "answer":"..."} ]
    Returns [] if the file is not found or an error occurs.
    """
    conversation_pairs = []
    if not os.path.isfile(json_path):
        print(f"Warning: JSON file not found: {json_path}")
        return conversation_pairs

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            for entry in data:
                q = entry.get("question", "").strip()
                a = entry.get("answer", "").strip()
                if q and a:
                    conversation_pairs.append([q, a])
    except Exception as e:
        print(f"Error loading JSON {json_path}: {e}")

    return conversation_pairs

def remove_duplicates(pairs):
    """
    Remove exact duplicate Q–A pairs.
    """
    unique_pairs = []
    seen = set()

    for q, a in pairs:
        combo = f"{q}||{a}"
        if combo not in seen:
            seen.add(combo)
            unique_pairs.append([q, a])

    return unique_pairs

def flatten_into_batches(pairs, batch_size=500):
    """
    Flatten Q–A pairs into larger conversation chunks so each chunk
    can be trained in a single .train() call, reducing overhead.
    """
    conversation_batch = []
    chunk_list = []
    count = 0

    for (q, a) in pairs:
        # Append Q then A to simulate a conversation segment
        conversation_batch.append(q)
        conversation_batch.append(a)
        count += 1

        if count >= batch_size:
            chunk_list.append(conversation_batch)
            conversation_batch = []
            count = 0

    # Handle any leftover
    if conversation_batch:
        chunk_list.append(conversation_batch)

    return chunk_list

def main():
    # 1) Load domain-specific pairs
    domain_pairs = load_conversation_pairs_from_json(DOMAIN_JSON_FILE)
    domain_pairs = domain_pairs or []  # Ensure it's not None

    print(f"Loaded {len(domain_pairs)} pairs from {DOMAIN_JSON_FILE}.")

    # 2) Remove duplicates
    domain_pairs = remove_duplicates(domain_pairs)
    print(f"Total pairs after removing duplicates: {len(domain_pairs)}")

    # 3) Optional: Flatten into conversation chunks for fewer .train() calls
    conversation_chunks = flatten_into_batches(domain_pairs, batch_size=500)

    # 4) Train on each chunk
    print("Training the chatbot on domain-only data. This may take some time...")
    for chunk in conversation_chunks:
        trainer.train(chunk)

    print("Training complete!")

    # 5) Quick test queries
    test_queries = [
        "How do I return a product?",
        "What is your refund policy?",
        "Is my personal data secure?",
    ]
    for query in test_queries:
        response = chatbot.get_response(query)
        print(f"\nUser Query: {query}")
        print(f"Bot Response: {response}\n")

if __name__ == "__main__":
    main()
