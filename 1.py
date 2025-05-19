import tkinter as tk
from tkinter import ttk
import time
import threading
import random
import os

tcl_path = "C:/Users/Nikhil Kartha/AppData/Local/Programs/Python/Python313/tcl/tcl8.6"
if "TCL_LIBRARY" not in os.environ or os.environ["TCL_LIBRARY"] != tcl_path:
    os.environ["TCL_LIBRARY"] = tcl_path


class ChatBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot UI")
        self.root.geometry("800x500")
        self.root.configure(bg="#f4f4f5")
        self.root.resizable(False, False)

        self.build_chat_frame()
        self.build_response_frame()
        self.build_config_frame()
        self.build_input_frame()
        self.build_analytics_frame()

    def build_chat_frame(self):
        self.chat_frame = tk.Frame(self.root, bg="white", bd=0, relief="flat")
        self.chat_frame.place(x=20, y=20, width=300, height=300)

        self.chat_log = tk.Text(
            self.chat_frame,
            wrap="word",
            state="disabled",
            bg="white",
            fg="black",
            font=("Arial", 10),
        )
        self.chat_log.pack(expand=True, fill="both")

        self.append_chat("User", "What’s the weather?")
        self.append_chat("Bot", "It looks sunny in Edinburgh today!")

    def append_chat(self, sender, message):
        self.chat_log.config(state="normal")
        self.chat_log.insert("end", f"{sender}: {message}\n")
        self.chat_log.config(state="disabled")
        self.chat_log.yview("end")

    def build_response_frame(self):
        self.response_frame = tk.LabelFrame(
            self.root,
            text="RESPONSES",
            bg="white",
            fg="black",
            font=("Arial", 9, "bold"),
        )
        self.response_frame.place(x=340, y=20, width=200, height=150)

        responses = ["It’s sunny today", "Let me check that", "→ Send message"]
        for i, text in enumerate(responses):
            b = tk.Button(
                self.response_frame,
                text=text,
                width=22,
                anchor="w",
                relief="groove",
                command=lambda t=text: self.append_chat("Bot", t),
            )
            b.pack(pady=3)

    def build_config_frame(self):
        self.config_frame = tk.LabelFrame(
            self.root,
            text="CONFIGURATION",
            bg="white",
            fg="black",
            font=("Arial", 9, "bold"),
        )
        self.config_frame.place(x=340, y=180, width=200, height=140)

        self.mic_var = tk.BooleanVar(value=True)
        mic_toggle = ttk.Checkbutton(
            self.config_frame, text="MIC ON", variable=self.mic_var
        )
        mic_toggle.pack(anchor="w", padx=10, pady=5)

        tk.Label(
            self.config_frame, text="LOGGING: Active", bg="white", font=("Arial", 9)
        ).pack(anchor="w", padx=10)
        tk.Label(
            self.config_frame, text="DELAY: 1.5s", bg="white", font=("Arial", 9)
        ).pack(anchor="w", padx=10)

    def build_input_frame(self):
        self.input_frame = tk.LabelFrame(
            self.root,
            text="USER INPUT",
            bg="white",
            fg="black",
            font=("Arial", 9, "bold"),
        )
        self.input_frame.place(x=20, y=340, width=520, height=120)

        tk.Label(self.input_frame, text="What’s the weather?", bg="white").pack(
            anchor="w", padx=10, pady=(5, 0)
        )

        # Container to hold Entry and Button side by side
        entry_container = tk.Frame(self.input_frame, bg="white")
        entry_container.pack(fill="x", padx=10, pady=10)

        self.input_entry = tk.Entry(entry_container)
        self.input_entry.pack(side="left", fill="x", expand=True)

        send_button = tk.Button(
            entry_container, text="SEND", width=10, command=self.send_user_input
        )
        send_button.pack(side="right", padx=(10, 0))

    def send_user_input(self):
        msg = self.input_entry.get().strip()
        if msg:
            self.append_chat("User", msg)
            self.input_entry.delete(0, "end")

    def build_analytics_frame(self):
        self.analytics_frame = tk.LabelFrame(
            self.root,
            text="ANALYTICS",
            bg="white",
            fg="black",
            font=("Arial", 9, "bold"),
        )
        self.analytics_frame.place(x=560, y=340, width=220, height=120)

        self.canvas = tk.Canvas(
            self.analytics_frame, bg="#f9fafb", height=80, width=200
        )
        self.canvas.pack(pady=10)

        self.draw_graph()

    def draw_graph(self):
        self.canvas.delete("all")
        values = [random.uniform(10, 80) for _ in range(6)]
        spacing = 200 // 5
        for i in range(5):
            x1 = i * spacing
            y1 = 80 - values[i]
            x2 = (i + 1) * spacing
            y2 = 80 - values[i + 1]
            self.canvas.create_line(x1, y1, x2, y2, fill="#4b5563", width=2)
        self.root.after(3000, self.draw_graph)  # update every 3 seconds


# Run the app
root = tk.Tk()
app = ChatBotApp(root)
root.mainloop()
