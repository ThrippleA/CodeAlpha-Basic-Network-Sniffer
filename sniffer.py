from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def packet_callback(packet):
    print("\n" + "=" * 60)
    print("NETWORK PACKET CAPTURED")
    print("=" * 60)

    if IP in packet:
        print(f"Source IP      : {packet[IP].src}")
        print(f"Destination IP : {packet[IP].dst}")

        if TCP in packet:
            print("Protocol       : TCP")
            print(f"Source Port    : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif UDP in packet:
            print("Protocol       : UDP")
            print(f"Source Port    : {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        elif ICMP in packet:
            print("Protocol       : ICMP")

        else:
            print(f"Protocol       : {packet[IP].proto}")

        if Raw in packet:
            print(f"Payload        : {bytes(packet[Raw].load)[:100]!r}")

    else:
        print("Non-IP packet captured")

print("Starting Network Sniffer...")
print("Interface: eth0")
print("Press CTRL+C to stop.")

sniff(iface="eth0", prn=packet_callback, store=False)
