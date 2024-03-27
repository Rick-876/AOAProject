#Group members:
#Kimone Bloomfield-2101557
#Monique Williams-1908929
#Fredrick Smith 2109221
# Javaughn Woolcock-

from chat_analyzer import ChatAnalyzer
from chat_gui import ChatGUI

class ChatApp:
    def __init__(self):
        # Initialize ChatAnalyzer and ChatGUI instances
        self.analyzer = ChatAnalyzer()  # Initialize the chat analyzer
        self.gui = ChatGUI(self.analyzer)  # Initialize the GUI with the analyzer

    def run(self):
        # Run the GUI
        self.gui.run()

if __name__ == "__main__":
    # If the script is executed directly, create a ChatApp instance and run it
    app = ChatApp()
    app.run()

