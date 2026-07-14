import threading

_running = False
_thread = None


def start(target_function):
    """
    Start conversation thread.
    """

    global _running
    global _thread

    if _running:
        return

    _running = True

    _thread = threading.Thread(
        target=target_function,
        daemon=True
    )

    _thread.start()


def stop():
    """
    Stop conversation.
    """

    global _running

    _running = False


def is_running():
    """
    Check if conversation is running.
    """

    return _running