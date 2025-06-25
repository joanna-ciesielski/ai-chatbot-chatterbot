from chatterbot import ChatBot

def main():
    chatbot = ChatBot(
        "DomainChatBot",
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri="sqlite:///my_chatbot_db.sqlite3",
        logic_adapters=["chatterbot.logic.BestMatch"]
    )

    print("Type 'quit' or 'exit' to stop chatting.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        bot_response = chatbot.get_response(user_input)
        print("Bot:", bot_response)

if __name__ == "__main__":
    main()
