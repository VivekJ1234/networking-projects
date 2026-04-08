import socket
import random

receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver_socket.bind(('localhost', 9999))

print("Receiver is running...")

expected_seq = 0

while True:
    data, addr = receiver_socket.recvfrom(1024)
    message = data.decode()

    seq, text = message.split(":", 1)
    seq = int(seq)

    print(f"Received packet {seq}: {text}")

    # simulate packet loss (20% chance)
    if random.random() < 0.2:
        print(f"Packet {seq} lost (simulated)")
        continue

    if seq == expected_seq:
        print(f"Packet {seq} accepted")
        expected_seq += 1
    else:
        print(f"Duplicate packet {seq} ignored")

    # send ACK
    ack = f"ACK:{seq}"
    receiver_socket.sendto(ack.encode(), addr)