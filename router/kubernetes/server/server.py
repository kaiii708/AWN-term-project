import socket
import time
from config import *
import random

# Server receive a connection from router, and send message to client through router.
# Server create the connection.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', SERVER_PORT))
server.listen(2)

# Server listen router connection request.
while True:
    routerConnection, address = server.accept()
    if (routerConnection != None):
        print(routerConnection)
        break

# Server sends a packet to client through router.
ethernet_header = ""
source_mac = SERVER_MAC
destination_mac = ROUTER_MAC
ethernet_header = ethernet_header + source_mac + destination_mac

source_ip = SERVER_IP
client_turn = 1
while True:
    IP_header = ""

    destination_ip = eval(f"CLIENT_{client_turn}_IP")
    IP_header = IP_header + source_ip + destination_ip
    message = f"\n{random.randint(0, 1000)} "
    packet = ethernet_header + IP_header + message

    # print("before sending")
    # print(f"source_mac:{packet[0:17]}")
    # print(f"destination_mac{packet[17:34]}")
    # print(f"source_ip{packet[34:45]}")
    # print(f"destination_ip{packet[45:56]}")
    # print(f"message{packet[56:]}")
    # print("start sending")
    routerConnection.send(bytes(packet, "utf-8"))
    client_turn += 1
    if client_turn == 4:
        client_turn = 1
    time.sleep(0.01)
