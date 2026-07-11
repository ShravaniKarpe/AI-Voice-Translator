import threading

conversation_running = False


def start(callback):
    global conversation_running

    conversation_running = True

    thread = threading.Thread(
        target=callback,
        daemon=True
    )

    thread.start()


def stop():
    global conversation_running
    conversation_running = False


def is_running():
    return conversation_running