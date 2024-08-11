from scapy.all import sniff, IP, TCP, UDP, ARP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        protocol = None

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"

        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        print(f"Protocol: {protocol}")

        if protocol == "TCP" or protocol == "UDP":
            try:
                payload = bytes(packet[protocol].payload)
                # Limit the payload to 50 characters for readability
                display_payload = payload[:50]
                print(f"Payload: {display_payload.decode('utf-8', 'ignore')}...")
            except Exception as e:
                print(f"Could not decode payload: {e}")

        print("-" * 50)
    
    elif ARP in packet:
        arp_layer = packet[ARP]
        print(f"ARP Packet: {arp_layer.summary()}")
        print("-" * 50)

def start_sniffing(interface):
    print(f"[*] Starting packet sniffing on interface: {interface}")
    try:
        sniff(iface=interface, prn=packet_callback, store=0)
    except KeyboardInterrupt:
        print("\n[*] Stopping packet sniffing.")
        return

if __name__ == "__main__":
    interface = "Wi-Fi"  # Change to your network interface name if different
    start_sniffing(interface)
