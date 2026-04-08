# Reliable Data Transfer over UDP

##  Overview
This project implements a reliable data transfer protocol over UDP using the Stop-and-Wait protocol.

Since UDP does not guarantee delivery, ordering, or reliability, this project simulates TCP-like reliability mechanisms.



##  Concepts Covered
- UDP communication
- Stop-and-Wait Protocol
- Sequence numbers
- Acknowledgements (ACK)
- Timeout & Retransmission



##  Features
- Reliable data transfer over UDP
- Packet loss simulation
- Automatic retransmission on timeout
- Sequence-based delivery



##  How It Works
1. Sender sends packet with sequence number
2. Receiver checks and sends ACK
3. If ACK not received → sender retransmits
4. Duplicate packets are ignored



## Sample Output
- Sender logs packet sending and retransmission
- Receiver logs packet reception and ACK



## Tech Stack
- Python
- Socket Programming