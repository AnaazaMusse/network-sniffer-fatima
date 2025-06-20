
from scapy.all import sniff, IP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"[+] Packet: {ip_layer.src} -> {ip_layer.dst} | Protocol: {ip_layer.proto}")

print("Starting network sniffer... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=0)
