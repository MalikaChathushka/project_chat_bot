# This file will handle the input/output interface for the chatbot
def start_chat():
    print("Welcome to the Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        yield user_input
