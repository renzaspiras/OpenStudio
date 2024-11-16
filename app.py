import tkinter as tk
import os

class TkinterApp:
    def __init__(self):
        # Load environment variables from .env file

        # Read the TITLE from environment variables
        self.title = "Open Studio"

        # Initialize the main window
        self.root = tk.Tk()
        self.root.title(self.title)

        # Set window size and position
        width = 1000
        height = 700
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def run(self):
        # Start the Tkinter event loop
        self.root.mainloop()

# Ensure this script runs only if executed directly
if __name__ == "__main__":
    app = TkinterApp()
    app.run()
