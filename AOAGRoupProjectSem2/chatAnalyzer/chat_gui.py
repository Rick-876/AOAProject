import tkinter as tk
from tkinter import ttk, filedialog
from chat_analyzer import ChatAnalyzer

class ChatGUI:
    def __init__(self, analyzer):
        self.analyzer = analyzer
        self.window = tk.Tk()
        self.window.title("Chat Participation Analyzer")
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for file selection and teacher entry
        self.file_frame = tk.Frame(self.window)
        self.file_frame.pack()

        # Label and entry for teacher's name
        tk.Label(self.file_frame, text="Teacher's Name:").grid(row=0, column=0)
        self.teacher_entry = tk.Entry(self.file_frame)
        self.teacher_entry.grid(row=0, column=1)

        # Button to browse and select a file
        browse_button = tk.Button(self.file_frame, text="Browse File", command=self.analyze_and_display)
        browse_button.grid(row=1, column=0, columnspan=2, pady=5)

        # Create a frame to display the participation data
        self.frame = tk.Frame(self.window)
        self.frame.pack()

        # Create Treeview widget
        self.tree = ttk.Treeview(self.frame, columns=("Name", "Responses", "Participation Grade"), show="headings")
        self.tree.heading("#1", text="Name")
        self.tree.heading("#2", text="Responses")
        self.tree.heading("#3", text="Grade")

        # Set column widths and alignment
        self.tree.column("#1", width=150, anchor="center")
        self.tree.column("#2", width=100, anchor="center")
        self.tree.column("#3", width=100, anchor="center")

        # Add Treeview to the frame
        self.tree.pack(fill="both", expand=True)

    def browse_file(self):
        try:
            filename = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
            if filename:
                with open(filename, "r") as file:
                    chat_lines = file.readlines()
                    return chat_lines
        except Exception as e:
            print("An error occurred while browsing/reading the file:", e)
        return None

    def analyze_and_display(self):
        chat_lines = self.browse_file()
        if chat_lines:
            teacher = self.teacher_entry.get()
            participation = self.analyzer.analyze_chat(chat_lines, teacher)
            
            # Clear previous data in Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Add data to Treeview
            for speaker, data in participation.items():
                self.tree.insert("", "end", text=speaker, values=(speaker, data["count"], data["grade"]))

    def run(self):
        self.window.mainloop()