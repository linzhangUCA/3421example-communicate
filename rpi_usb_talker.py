import serial
from time import sleep

# SETUP
messenger = serial.Serial(port='/dev/ttyACM0', baudrate=115200)
print(messenger.name)

# LOOP
for i in range(10):
    msg = f"Hello from RPi: {i}\n".encode('utf-8')
    messenger.write(msg)
    # if messenger.inWaiting() > 0:
    #     pico_data = messenger.readline()
    #     pico_data = pico_data.decode('utf-8', 'ignore')
    #     print(pico_data)
    sleep(1)
messenger.close()
