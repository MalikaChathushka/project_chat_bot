# This file will contain patterns for matching user input and generating appropriate responses
patterns = {
    r"hi|hello|hey": [
        "Hi there! How can I help you today?",
        "Hello! How's it going?",
        "Hey! What can I do for you?"
    ],
    r"how are you|what's up": [
        "I'm just a bot, but I'm doing great! How about you?",
        "I'm feeling digital! How are you?"
    ],
    r"what is your name": [
        "I'm your friendly chatbot, ChatGPT.",
        "You can call me Chatbot, at your service."
    ],
    r"bye|goodbye": [
        "Goodbye! Have a nice day!",
        "See you later! Don't hesitate to reach out again!"
    ],
    # Add more patterns and responses here for extended functionality
    r"what is the meaning of life": [
        "The meaning of life is a profound question, but for now, how about enjoying a good chat?",
        "42, of course! Just kidding. It’s all about living your best life!"
    ],
}
