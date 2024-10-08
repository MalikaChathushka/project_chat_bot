# This file will contain the logic for handling inputs and generating responses
import re
from response_patterns import patterns

class BotLogic:
    def __init__(self):
        # We could load more advanced data here if needed
        pass

    def get_response(self, user_input):
        user_input = user_input.lower()
        for pattern, responses in patterns.items():
            if re.search(pattern, user_input):
                return self._select_response(responses)
        return "Sorry, I didn't quite understand that."

    def _select_response(self, responses):
        # Randomize responses or select based on some logic
        import random
        return random.choice(responses)
