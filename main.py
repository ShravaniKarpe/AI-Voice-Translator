import customtkinter as ctk

from speech import recognize_speech
from translator import translate_text
from tts import speak
import conversation

# ---------------- APP SETTINGS ---------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🌍 AI Voice Translator")
app.geometry("900x650")

languages = [
    "English",
    "Marathi",
    "Hindi",
    "Tamil",
    "Telugu"
]

# ---------------- FUNCTIONS ---------------- #

def listen():

    language = source_menu.get()

    text = recognize_speech(language)

    if not text:
        return

    original_box.delete("1.0", "end")
    original_box.insert("end", text)

    translated = translate_text(
        text,
        source_menu.get(),
        target_menu.get()
    )

    translated_box.delete("1.0", "end")
    translated_box.insert("end", translated)


def speak_translation():

    text = translated_box.get("1.0", "end").strip()

    if text:
        speak(text, target_menu.get())


def swap_languages():

    source = source_menu.get()
    target = target_menu.get()

    source_menu.set(target)
    target_menu.set(source)


# ---------------- CONVERSATION MODE ---------------- #

def start_conversation():

    original_box.delete("1.0", "end")
    translated_box.delete("1.0", "end")

    conversation.start(conversation_loop)


def conversation_loop():

    while conversation.is_running():

        try:

            text = recognize_speech(source_menu.get())

            if not text:
                continue

            translated = translate_text(
                text,
                source_menu.get(),
                target_menu.get()
            )

            app.after(
                0,
                lambda t=text: (
                    original_box.insert("end", f"\n👤 {t}\n"),
                    original_box.see("end")
                )
            )

            app.after(
                0,
                lambda tr=translated: (
                    translated_box.insert("end", f"\n🤖 {tr}\n"),
                    translated_box.see("end")
                )
            )

            speak(translated, target_menu.get())

        except Exception as e:
            print("Conversation Error:", e)


# ---------------- TITLE ---------------- #

title = ctk.CTkLabel(
    app,
    text="🌍 AI Voice Translator",
    font=("Arial", 30, "bold")
)

title.pack(pady=20)

# ---------------- LANGUAGE FRAME ---------------- #

frame = ctk.CTkFrame(app)
frame.pack(fill="x", padx=20, pady=10)

source_menu = ctk.CTkOptionMenu(
    frame,
    values=languages
)

source_menu.set("English")
source_menu.pack(side="left", padx=20, pady=15)

target_menu = ctk.CTkOptionMenu(
    frame,
    values=languages
)

target_menu.set("Marathi")
target_menu.pack(side="right", padx=20, pady=15)

# ---------------- ORIGINAL TEXT ---------------- #

label1 = ctk.CTkLabel(
    app,
    text="Original Speech",
    font=("Arial", 18, "bold")
)

label1.pack()

original_box = ctk.CTkTextbox(
    app,
    width=800,
    height=150
)

original_box.pack(pady=10)

# ---------------- TRANSLATED TEXT ---------------- #

label2 = ctk.CTkLabel(
    app,
    text="Translated Speech",
    font=("Arial", 18, "bold")
)

label2.pack()

translated_box = ctk.CTkTextbox(
    app,
    width=800,
    height=150
)

translated_box.pack(pady=10)

# ---------------- BUTTONS ---------------- #

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=25)

listen_btn = ctk.CTkButton(
    button_frame,
    text="🎤 Listen",
    width=130,
    command=listen
)

listen_btn.grid(row=0, column=0, padx=8)

speak_btn = ctk.CTkButton(
    button_frame,
    text="🔊 Speak",
    width=130,
    command=speak_translation
)

speak_btn.grid(row=0, column=1, padx=8)

swap_btn = ctk.CTkButton(
    button_frame,
    text="🔄 Swap",
    width=130,
    command=swap_languages
)

swap_btn.grid(row=0, column=2, padx=8)

start_btn = ctk.CTkButton(
    button_frame,
    text="🟢 Start Conversation",
    width=170,
    command=start_conversation
)

start_btn.grid(row=0, column=3, padx=8)

stop_btn = ctk.CTkButton(
    button_frame,
    text="🔴 Stop Conversation",
    width=170,
    fg_color="red",
    hover_color="#AA0000",
    command=conversation.stop
)

stop_btn.grid(row=0, column=4, padx=8)

exit_btn = ctk.CTkButton(
    button_frame,
    text="❌ Exit",
    width=130,
    command=app.destroy
)

exit_btn.grid(row=0, column=5, padx=8)

# ---------------- RUN APP ---------------- #

app.mainloop()

