import matplotlib.pyplot as plt
import random

time_steps = 30

# TCP Tahoe 
def simulate_tahoe():
    cwnd = 1
    ssthresh = 16
    values = []

    for t in range(time_steps):
        values.append(cwnd)
        print(f"[Tahoe] Time {t}: cwnd = {cwnd}")

        # random packet loss (10% chance)
        if random.random() < 0.1:
            ssthresh = max(cwnd // 2, 1)
            print(f"[Tahoe] Packet loss at {t}, new ssthresh={ssthresh}")
            cwnd = 1
            continue

        if cwnd < ssthresh:
            cwnd *= 2   # slow start (exponential)
        else:
            cwnd += 1   # congestion avoidance (linear)

    return values


# TCP Reno 
def simulate_reno():
    cwnd = 1
    ssthresh = 16
    values = []

    for t in range(time_steps):
        values.append(cwnd)
        print(f"[Reno] Time {t}: cwnd = {cwnd}")

        # random packet loss (10% chance)
        if random.random() < 0.1:
            ssthresh = max(cwnd // 2, 1)
            print(f"[Reno] Packet loss at {t}, new ssthresh={ssthresh}")
            cwnd = ssthresh   # Reno difference
            continue

        if cwnd < ssthresh:
            cwnd *= 2
        else:
            cwnd += 1

    return values


# Run Simulation 
tahoe = simulate_tahoe()
print("\n----------------------------\n")
reno = simulate_reno()

# ------------------ Metrics ------------------
print("\n=== Performance Comparison ===")
print("Average cwnd (Tahoe):", sum(tahoe) / len(tahoe))
print("Average cwnd (Reno):", sum(reno) / len(reno))


# ------------------ Plot ------------------
plt.plot(tahoe, label="TCP Tahoe", marker='o')
plt.plot(reno, label="TCP Reno", marker='x')

plt.title("TCP Congestion Control: Tahoe vs Reno")
plt.xlabel("Time (RTT)")
plt.ylabel("Congestion Window (cwnd)")
plt.legend()
plt.grid()

plt.show()