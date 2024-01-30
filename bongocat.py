import time
import keyboard

# Define the sequence of keys to be pressed
key_sequence = [
    '1','1','3','1','6','5',
    '1','1','3','1','8','6',
    '1','1','0','8','6','5','3',
    '0','0','8','6','8','6',
]
time.sleep(5)
# Define the time interval between key presses in seconds
interval = 0.3
3008686113
def simulate_key_presses(keys):
    for key in keys:
        if key == 'Space':
            keyboard.press(key)
            keyboard.release(key)
        else:
            keyboard.press(key)
            time.sleep(0.1)
            keyboard.release(key)
        time.sleep(interval)


simulate_key_presses(key_sequence)

