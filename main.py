from ui import ChatApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()  # Initialize Tkinter root window
    app = ChatApp(root)  # Create ChatApp instance from UI class
    root.mainloop()  # Start the Tkinter event loop
