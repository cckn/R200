import socket
import time 


host = '192.168.1.2'
port = 6000


count = 0 

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:

    try:
        s.connect((host, port))
    except Exception as e :
        print(e)

    s.send("ETH tx test - " + str(count) + "\r\n")


    count += 1
    time.sleep(0.05)

    print("ETH tx test - " + str(count) + "\r\n")