import time
import serial

count = 0


while True:

    with serial.Serial(port='/dev/serial0',baudrate=9600) as s:
        s.write("rs485 0 tx test - " + str(count) + "\r\n")

    with serial.Serial(port='/dev/serial1',baudrate=9600) as s:
        s.write("rs485 1 tx test - " + str(count) + "\r\n")

    try:
        with serial.Serial(port='/dev/ttyUSB0',baudrate=9600) as s:
            s.write("USB tx test - " + str(count) + "\r\n")
    except Exception as e:
        print(e)

    try:
        with serial.Serial(port='/dev/ttyUSB1',baudrate=9600) as s:
            s.write("USB tx test - " + str(count) + "\r\n")
    except Exception as e:
        print(e)
        
    try:
        with serial.Serial(port='/dev/ttyUSB2',baudrate=9600) as s:
            s.write("USB tx test - " + str(count) + "\r\n")
    except Exception as e:
        print(e)

    count +=  1
    time.sleep(0.05)

    print("serial test - " + str(count) + "\r\n")
