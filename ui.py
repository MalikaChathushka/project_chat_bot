# This file will handle the input/output interface for the chatbot
import tkinter as tk
from tkinter import scrolledtext
from bot_logic import BotLogic
from utils import get_timestamp


class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mcstang ChatBot")

        # Customize window background color
        self.root.configure(bg='#075E54')

        # Chat history (scrollable)
        self.chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Arial", 12),
                                                     bg='#DCF8C6')
        self.chat_window.config(state=tk.DISABLED)
        self.chat_window.pack(pady=10)

        # User input text field
        self.user_input = tk.Entry(root, font=("Arial", 12), width=40, bg='#ECE5DD')
        self.user_input.pack(pady=5, padx=5, side=tk.LEFT)
        self.user_input.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message, font=("Arial", 12), bg='#25D366',
                                     fg='white')
        self.send_button.pack(pady=5, padx=5, side=tk.RIGHT)

        # Bot logic instance
        self.bot = BotLogic()

    def send_message(self, event=None):
        user_message = self.user_input.get()
        if user_message:
            self.display_message(f"You: {user_message}\n", user=True)
            bot_response = self.bot.get_response(user_message)
            self.display_message(f"Bot: {bot_response}\n", user=False)
        self.user_input.delete(0, tk.END)

    def display_message(self, message, user=True):
        self.chat_window.config(state=tk.NORMAL)
        timestamp = get_timestamp()

        if user:
            formatted_message = f"{message.strip()} [{timestamp}]\n"
            self.chat_window.insert(tk.END, formatted_message, 'user_message')
        else:
            formatted_message = f"{message.strip()} [{timestamp}]\n"
            self.chat_window.insert(tk.END, formatted_message, 'bot_message')

        self.chat_window.tag_config('user_message', foreground='#25D366', font=("Arial", 12, "bold"))
        self.chat_window.tag_config('bot_message', foreground='#075E54', font=("Arial", 12, "italic"))

        self.chat_window.config(state=tk.DISABLED)
        self.chat_window.yview(tk.END)

