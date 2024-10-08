# This file will contain patterns for matching user input and generating appropriate responses.
import re

def get_response(user_input):
    patterns = {
        "hello": r"hello|hi|hey",
        "how are you": r"how are you|how's it going",
        "bye": r"bye|goodbye"
    }

    for response, pattern in patterns.items():
        if re.search(pattern, user_input.lower()):
            return response.capitalize()

    return "Sorry, I don't understand."
