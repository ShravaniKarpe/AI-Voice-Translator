from datetime import datetime
import os

conversation_history = []


def add_history(source_lang, target_lang, original_text, translated_text):

    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    entry = {
        "time": current_time,
        "source": source_lang,
        "target": target_lang,
        "original": original_text,
        "translated": translated_text
    }

    conversation_history.append(entry)


def get_history():

    result = ""

    for item in conversation_history:

        result += (
            f"🕒 {item['time']}\n"
            f"{item['source']}:\n"
            f"{item['original']}\n\n"
            f"{item['target']}:\n"
            f"{item['translated']}\n"
            f"{'-'*50}\n\n"
        )

    return result


def clear_history():

    conversation_history.clear()


def save_history():

    if not conversation_history:
        return None

    if not os.path.exists("conversations"):
        os.makedirs("conversations")

    filename = datetime.now().strftime(
        "conversations/conversation_%Y%m%d_%H%M%S.txt"
    )

    with open(filename, "w", encoding="utf-8") as file:

        file.write(get_history())

    return filename