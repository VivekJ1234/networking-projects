import socket
import time

sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver_address = ('localhost', 9999)

messages = ["Hello", "This", "Is", "UDP", "Reliable", "Transfer"]

seq = 0

for msg in messages:
    while True:
        packet = f"{seq}:{msg}"
        sender_socket.sendto(packet.encode(), receiver_address)
        print(f"Sent packet {seq}: {msg}")

        sender_socket.settimeout(2)

        try:
            ack, _ = sender_socket.recvfrom(1024)
            ack = ack.decode()

            if ack == f"ACK:{seq}":
                print(f"Received ACK for {seq}\n")
                seq += 1
                break

        except socket.timeout:
            print(f"Timeout! Resending packet {seq}...\n")

sender_socket.close()