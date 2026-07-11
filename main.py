import customtkinter as ctk

from speech import recognize_speech
from translator import translate_text
from tts import speak

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

# ---------------- FUNCTIONS -------------
    
def listen():

    language = source_menu.get()

    text = recognize_speech(language)

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

    if text != "":
        speak(text, target_menu.get())

def swap_languages():

    source = source_menu.get()

    target = target_menu.get()

    source_menu.set(target)

    target_menu.set(source)

# ---------------- TITLE ---------------- #

title = ctk.CTkLabel(
    app,
    text="🌍 AI Voice Translator",
    font=("Arial",30,"bold")
)

title.pack(pady=20)

# ---------------- DROPDOWNS ---------------- #

frame = ctk.CTkFrame(app)

frame.pack(fill="x",padx=20,pady=10)

source_menu = ctk.CTkOptionMenu(
    frame,
    values=languages
)

source_menu.set("English")

source_menu.pack(side="left",padx=20,pady=15)

target_menu = ctk.CTkOptionMenu(
    frame,
    values=languages
)

target_menu.set("Marathi")

target_menu.pack(side="right",padx=20,pady=15)

# ---------------- ORIGINAL ---------------- #

label1 = ctk.CTkLabel(
    app,
    text="Original Speech",
    font=("Arial",18,"bold")
)

label1.pack()

original_box = ctk.CTkTextbox(
    app,
    width=800,
    height=120
)

original_box.pack(pady=10)

# ---------------- TRANSLATED ---------------- #

label2 = ctk.CTkLabel(
    app,
    text="Translated Speech",
    font=("Arial",18,"bold")
)

label2.pack()

translated_box = ctk.CTkTextbox(
    app,
    width=800,
    height=120
)

translated_box.pack(pady=10)

# ---------------- BUTTONS ---------------- #

button_frame = ctk.CTkFrame(app)

button_frame.pack(pady=25)

listen_btn = ctk.CTkButton(
    button_frame,
    text="🎤 Listen",
    width=150,
    command=listen
)

listen_btn.grid(row=0,column=0,padx=15)

speak_btn = ctk.CTkButton(
    button_frame,
    text="🔊 Speak",
    width=150,
    command=speak_translation
)

speak_btn.grid(row=0,column=1,padx=15)

swap_btn = ctk.CTkButton(
    button_frame,
    text="🔄 Swap",
    width=150,
    command=swap_languages
)

swap_btn.grid(row=0,column=2,padx=15)

exit_btn = ctk.CTkButton(
    button_frame,
    text="❌ Exit",
    width=150,
    command=app.destroy
)

exit_btn.grid(row=0,column=3,padx=15)

app.mainloop()