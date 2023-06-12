import socket
import time 
from config import *

# Client create connection to router, and receive  server message from router.
# Client connect to router.
router = ("localhost", ROUTER_PORT_2)
client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
time.sleep(1)
client1.connect(router)

# Client receive server message from router.
while True:
    received_message = client1.recv(1024)
    received_message = received_message.decode("utf-8")
    source_mac = received_message[0:17]
    destination_mac = received_message[17:34]
    source_ip = received_message[34:45]
    destination_ip =  received_message[45:56]
    message = received_message[56:]
    print("\nPacket integrity:\ndestination MAC address matches client 1 MAC address: {mac}".format(mac=(CLIENT_1_MAC == destination_mac)))
    print("\ndestination IP address matches client 1 IP address: {mac}".format(mac=(CLIENT_1_IP == destination_ip)))
    print("\nThe packed received:\n Source MAC address: {source_mac}, Destination MAC address: {destination_mac}".format(source_mac=source_mac, destination_mac=destination_mac))
    print("\nSource IP address: {source_ip}, Destination IP address: {destination_ip}".format(source_ip=source_ip, destination_ip=destination_ip))
    print("\nMessage: " + message)