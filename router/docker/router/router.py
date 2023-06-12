import socket
import time
from config import *


# Router listen for client connection requests, and connect to server. Then forward the message from
# server to specific client.
# Router create a server for receiving client connection request.
router_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
router_send.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
router_send.bind(("0.0.0.0", ROUTER_PORT_2))

# Router listen the connection request, and record the client socket to client1, client2, and client3.
router_send.listen(4)
client1 = None
client2 = None
client3 = None
while (client1 == None or client2 == None or client3 == None):
    client, address = router_send.accept()
    
    if(client1 == None):
        client1 = client
        print("Client 1 is online")
    elif(client2 == None):
        client2 = client
        print("Client 2 is online")
    else:
        client3 = client
        print("Client 3 is online")

# Create ARP table.
arp_table_socket = {CLIENT_1_IP : client1, CLIENT_2_IP : client2, CLIENT_3_IP : client3}
arp_table_mac = {CLIENT_1_IP : CLIENT_1_MAC, CLIENT_2_IP : CLIENT_2_MAC, CLIENT_3_IP : CLIENT_3_MAC}

# Router create a connection for connecting the server.
router = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
router.bind(("0.0.0.0", ROUTER_PORT_1))
server = (("server", SERVER_PORT))
router.connect(server)

# Router receive the message from server and forward to specific client.
while True:
    received_message = router.recv(1024)
    received_message =  received_message.decode("utf-8")
    
    source_mac = received_message[0:17]
    destination_mac = received_message[17:34]
    source_ip = received_message[34:45]
    destination_ip =  received_message[45:56]
    message = received_message[56:]
    
    print("The packed received:\n Source MAC address: {source_mac}, Destination MAC address: {destination_mac}".format(source_mac=source_mac, destination_mac=destination_mac))
    print("\nSource IP address: {source_ip}, Destination IP address: {destination_ip}".format(source_ip=source_ip, destination_ip=destination_ip))
    print("\nMessage: " + message)
    
    ethernet_header = ROUTER_MAC + arp_table_mac[destination_ip]
    IP_header = source_ip + destination_ip
    packet = ethernet_header + IP_header + message

    destination_socket = arp_table_socket[destination_ip]
    
    destination_socket.send(bytes(packet, "utf-8"))
    # time.sleep(2)