"""
Run this code on Pico (uPython).
Rename to [main.py] for auto start.
"""
import sys
import select

# SETUP
listener = select.poll()
listener.register(sys.stdin, select.POLLIN)
event = listener.poll()

# LOOP
while True:
    # read data from serial
    for msg, _ in event:
        buffer = msg.readline().rstrip()
        print(buffer)
        # if len(buffer) == 17: # Hello from RPi: 0
        #     print(f"Pico hears: {buffer}")
            # sys.stdout.write(buffer)
