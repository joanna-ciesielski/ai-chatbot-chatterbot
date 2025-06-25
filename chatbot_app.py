"""
chatbot_app.py
This script loads a previously trained ChatterBot model/database and provides
an interface for chatting with the bot.
"""

from chatterbot import ChatBot

def main():
    # Provide the same settings used in training (but skip re-training).
    chatbot = ChatBot(
        "CustomerSupportBot",
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:////Volumes/Seagate/CSC525/my_chatbot_db.sqlite3',
        # ^ Use the absolute path to your actual database file
        logic_adapters=['chatterbot.logic.BestMatch']
    )

    print("ChatBot loaded. Type 'quit' or 'exit' to end the session.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Bot: Goodbye!")
            break
        bot_response = chatbot.get_response(user_input)
        print(f"Bot: {bot_response}")

if __name__ == "__main__":
    main()
