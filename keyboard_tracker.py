"""
Keyboard tracker MVP.
"""

import pynput


def on_press(key):
    """
    Defines keyboard listener's behavior when a key is pressed.

    """
    if key == pynput.keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except AttributeError:
        k = key.name  # other keys

    if k in ["f1", "f2"]:  # keys of interest
        print(k)

    return None


listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread

print("It has started listening.")

listener.join()  # remove if main thread is polling self.keys

print("It has stopped listening.")
