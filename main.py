import customtkinter as ctk
from tkinter import messagebox
import threading

from speech import recognize_speech
from translator import translate_text
from tts import speak

import conversation

from history import (
    add_history,
    get_history,
    clear_history,
    save_history
)

# ---------------- APP ---------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("🌍 AI Voice Translator V3")

app.geometry("1200x900")

app.resizable(True, True)

# ---------------- Languages ---------------- #

languages = [
    "English",
    "Hindi",
    "Marathi",
    "Tamil",
    "Telugu",
    "Kannada",
    "Malayalam",
    "Gujarati",
    "Punjabi",
    "Bengali",
    "Odia",
    "French",
    "German",
    "Spanish",
    "Japanese"
]

# ---------------- Title ---------------- #

title = ctk.CTkLabel(
    app,
    text="🌍 AI Voice Translator",
    font=("Arial",30,"bold")
)

title.pack(pady=10)

# ---------------- Language Frame ---------------- #

language_frame = ctk.CTkFrame(app)

language_frame.pack(
    fill="x",
    padx=20,
    pady=10
)

source_menu = ctk.CTkOptionMenu(
    language_frame,
    values=languages,
    width=220
)

source_menu.set("English")

source_menu.pack(
    side="left",
    padx=20,
    pady=15
)

target_menu = ctk.CTkOptionMenu(
    language_frame,
    values=languages,
    width=220
)

target_menu.set("Marathi")

target_menu.pack(
    side="right",
    padx=20,
    pady=15
)

# ---------------- Original ---------------- #

label1 = ctk.CTkLabel(
    app,
    text="🎤 Original Speech",
    font=("Arial",18,"bold")
)

label1.pack()

original_box = ctk.CTkTextbox(
    app,
    width=1050,
    height=90
)

original_box.pack(pady=10)

# ---------------- Translation ---------------- #

label2 = ctk.CTkLabel(
    app,
    text="🌐 Translation",
    font=("Arial",18,"bold")
)

label2.pack()

translated_box = ctk.CTkTextbox(
    app,
    width=1050,
    height=90
)

translated_box.pack(pady=10)

# ---------------- History ---------------- #

history_label = ctk.CTkLabel(
    app,
    text="📜 Conversation History",
    font=("Arial",18,"bold")
)

history_label.pack()

history_box = ctk.CTkTextbox(
    app,
    width=1050,
    height=80
)

history_box.pack(pady=10)

# ---------------- FUNCTIONS ---------------- #

def listen():

    text = recognize_speech(
        source_menu.get()
    )

    if not text:
        return

    original_box.delete("1.0","end")
    original_box.insert("end",text)

    translated = translate_text(
        text,
        source_menu.get(),
        target_menu.get()
    )

    translated_box.delete("1.0","end")
    translated_box.insert("end",translated)

    add_history(
        source_menu.get(),
        target_menu.get(),
        text,
        translated
    )

    history_box.delete("1.0","end")
    history_box.insert(
        "end",
        get_history()
    )

def speak_translation():

    text = translated_box.get(
        "1.0",
        "end"
    ).strip()

    if text:
        speak(
            text,
            target_menu.get()
        )

def swap_languages():

    s = source_menu.get()

    t = target_menu.get()

    source_menu.set(t)

    target_menu.set(s)
    # ---------------- MORE FUNCTIONS ---------------- #

def clear_all():

    original_box.delete("1.0", "end")
    translated_box.delete("1.0", "end")
    history_box.delete("1.0", "end")

    clear_history()


def copy_translation():

    text = translated_box.get("1.0", "end").strip()

    if text:
        app.clipboard_clear()
        app.clipboard_append(text)

        messagebox.showinfo(
            "Copied",
            "Translation copied to clipboard!"
        )


def save_conversation():

    filename = save_history()

    if filename:
        messagebox.showinfo(
            "Saved",
            f"Conversation saved as:\n{filename}"
        )


# ---------------- Conversation ---------------- #

def conversation_loop():

    while conversation.is_running():

        text = recognize_speech(
            source_menu.get()
        )

        if (
            not text
            or text.startswith("Error")
            or text == "Could not understand."
        ):
            continue

        translated = translate_text(
            text,
            source_menu.get(),
            target_menu.get()
        )

        app.after(
            0,
            lambda t=text: (
                original_box.delete("1.0", "end"),
                original_box.insert("end", t)
            )
        )

        app.after(
            0,
            lambda tr=translated: (
                translated_box.delete("1.0", "end"),
                translated_box.insert("end", tr)
            )
        )

        add_history(
            source_menu.get(),
            target_menu.get(),
            text,
            translated
        )

        app.after(
            0,
            lambda: (
                history_box.delete("1.0", "end"),
                history_box.insert("end", get_history())
            )
        )

        speak(
            translated,
            target_menu.get()
        )


def start_conversation():

    conversation.start(
        conversation_loop
    )


def stop_conversation():

    conversation.stop()

# ---------------- BUTTON FRAME ---------------- #

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=15)

# ---------- First Row ---------- #

listen_btn = ctk.CTkButton(
    button_frame,
    text="🎤 Listen",
    width=130,
    command=listen
)
listen_btn.grid(row=0, column=0, padx=5, pady=5)

speak_btn = ctk.CTkButton(
    button_frame,
    text="🔊 Speak",
    width=130,
    command=speak_translation
)
speak_btn.grid(row=0, column=1, padx=5, pady=5)

swap_btn = ctk.CTkButton(
    button_frame,
    text="🔄 Swap",
    width=130,
    command=swap_languages
)
swap_btn.grid(row=0, column=2, padx=5, pady=5)

copy_btn = ctk.CTkButton(
    button_frame,
    text="📋 Copy",
    width=130,
    command=copy_translation
)
copy_btn.grid(row=0, column=3, padx=5, pady=5)

# ---------- Second Row ---------- #

clear_btn = ctk.CTkButton(
    button_frame,
    text="🗑 Clear",
    width=130,
    command=clear_all
)
clear_btn.grid(row=1, column=0, padx=5, pady=5)

save_btn = ctk.CTkButton(
    button_frame,
    text="💾 Save",
    width=130,
    command=save_conversation
)
save_btn.grid(row=1, column=1, padx=5, pady=5)

start_btn = ctk.CTkButton(
    button_frame,
    text="🟢 Start",
    width=130,
    fg_color="#2E8B57",
    hover_color="#3CB371",
    command=start_conversation
)
start_btn.grid(row=1, column=2, padx=5, pady=5)

stop_btn = ctk.CTkButton(
    button_frame,
    text="🔴 Stop",
    width=130,
    fg_color="red",
    hover_color="#990000",
    command=stop_conversation
)
stop_btn.grid(row=1, column=3, padx=5, pady=5)

# ---------- Exit Button ---------- #

exit_btn = ctk.CTkButton(
    app,
    text="❌ Exit",
    width=220,
    fg_color="#444444",
    hover_color="#222222",
    command=app.destroy
)

exit_btn.pack(pady=10)
# ---------------- LOAD HISTORY ON STARTUP ---------------- #

try:
    history_box.delete("1.0", "end")
    history_box.insert("end", get_history())
except Exception:
    pass


# ---------------- KEYBOARD SHORTCUTS ---------------- #

def copy_shortcut(event):
    copy_translation()


app.bind("<Control-c>", copy_shortcut)


# ---------------- WINDOW CLOSE ---------------- #

def on_closing():

    try:
        conversation.stop()
    except Exception:
        pass

    app.destroy()


app.protocol("WM_DELETE_WINDOW", on_closing)


# ---------------- START APPLICATION ---------------- #

app.mainloop()
