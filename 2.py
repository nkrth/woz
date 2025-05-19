import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import openai
import requests
import os
from dotenv import load_dotenv
from PIL import Image, ImageTk

tcl_path = "C:/Users/Nikhil Kartha/AppData/Local/Programs/Python/Python313/tcl/tcl8.6"
if 'TCL_LIBRARY' not in os.environ or os.environ['TCL_LIBRARY'] != tcl_path:
    os.environ['TCL_LIBRARY'] = tcl_path

# Load environment variables
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to check internet connection
def check_internet():
    try:
        requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Function to get response from OpenAI
def get_openai_response(prompt):
    if check_internet():
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    else:
        return "No internet connection. Please try again later."

# Function to simulate local LLM response
def get_local_llm_response(prompt):
    return f"Local LLM response to: {prompt}"

# Function to handle user input and get responses
def handle_input():
    user_input = entry.get()
    if user_input:
        local_response = get_local_llm_response(user_input)
        openai_response = get_openai_response(user_input)

        # Display responses in the text box
        text.insert(tk.END, f"You: {user_input}\n", 'user')
        text.insert(tk.END, f"Local LLM: {local_response}\n", 'local')
        text.insert(tk.END, f"OpenAI: {openai_response}\n\n", 'bot')

        # Clear the entry box
        entry.delete(0, tk.END)

        # Scroll to the end of the text box
        text.see(tk.END)

# Function to send emotion to the bot
def send_emotion(emotion):
    emotion_response = f"Emotion sent: {emotion}"
    text.insert(tk.END, f"You: {emotion_response}\n", 'user')
    local_response = get_local_llm_response(emotion_response)
    openai_response = get_openai_response(emotion_response)
    text.insert(tk.END, f"Local LLM: {local_response}\n", 'local')
    text.insert(tk.END, f"OpenAI: {openai_response}\n\n", 'bot')
    text.see(tk.END)

# Create the main window with ttkbootstrap
style = Style()
window = style.master
window.title("Chat with CPU")
window.geometry("800x500")

# Create a multi-line text box
text = tk.Text(master=window, wrap=tk.WORD, height=15)
text.pack(expand=True, fill=tk.BOTH)

# Create a single-line entry
entry = ttk.Entry(master=window)
entry.pack(fill=tk.X)

# Create a button to send the input
send_button = ttk.Button(master=window, text="Send", command=handle_input)
send_button.pack()

# Emotion buttons
emotions = ["Happy", "Sad", "Angry", "Surprised"]
for emotion in emotions:
    emotion_button = ttk.Button(master=window, text=emotion, command=lambda e=emotion: send_emotion(e))
    emotion_button.pack(side=tk.LEFT, padx=5)

# Load and display avatars
user_avatar = Image.open("user_avatar.png").resize((40, 40), Image.LANCZOS)
bot_avatar = Image.open("bot_avatar.jpg").resize((40, 40), Image.LANCZOS)

user_avatar = ImageTk.PhotoImage(user_avatar)
bot_avatar = ImageTk.PhotoImage(bot_avatar)

# Create labels for avatars
user_label = ttk.Label(window, image=user_avatar)
user_label.image = user_avatar  # Keep a reference
user_label.pack(side=tk.LEFT, padx=5)

bot_label = ttk.Label(window, image=bot_avatar)
bot_label.image = bot_avatar  # Keep a reference
bot_label.pack(side=tk.RIGHT, padx=5)

# Add tags for text colors
text.tag_config('user', foreground='blue')
text.tag_config('local', foreground='green')
text.tag_config('bot', foreground='orange')

# Start the main loop
window.mainloop()
