from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

packet_count = 0

def packet_callback(packet):
    global packet_count
    packet_count += 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n" + "=" * 60)
    print(f"PACKET NUMBER: {packet_count}")
    print(f"TIME: {timestamp}")
    print("=" * 60)

    if IP in packet:
        print(f"Source IP       : {packet[IP].src}")
        print(f"Destination IP  : {packet[IP].dst}")

        if TCP in packet:
            print("Protocol        : TCP")
            print(f"Source Port     : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif UDP in packet:
            print("Protocol        : UDP")
            print(f"Source Port     : {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        elif ICMP in packet:
            print("Protocol        : ICMP")
        else:
            print(f"Protocol        : {packet[IP].proto}")

        if Raw in packet:
            print(f"Payload         : {bytes(packet[Raw].load)[:100]!r}")
    else:
        print("Non-IP packet captured")


print("============================================")
print("       BASIC NETWORK PACKET SNIFFER")
print("============================================")
print("Interface: eth0")
print("Press CTRL+C to stop capturing.")

try:
    sniff(iface="eth0", prn=packet_callback, store=False)
except KeyboardInterrupt:
    print("\nSniffer stopped.")
    print(f"Total packets captured: {packet_count}")
