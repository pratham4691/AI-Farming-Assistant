import scapy.all as scapy
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.l2 import Ether
from datetime import datetime

def dissect_packet(packet):
    print("="*80)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")
    if Ether in packet:
        eth = packet[Ether]
        print(f"Ethernet: {eth.src} -> {eth.dst} | Type: {hex(eth.type)}")
    if IP in packet:
        ip = packet[IP]
        print(f"IP: {ip.src} -> {ip.dst} | TTL: {ip.ttl} | Proto: {ip.proto}")
        proto = ip.proto
        if proto == 6 and TCP in packet:
            tcp = packet[TCP]
            print(f"TCP: {tcp.sport} -> {tcp.dport} | Flags: {tcp.flags} | Seq: {tcp.seq} | Ack: {tcp.ack}")
            if tcp.payload:
                print(f"TCP Payload ({len(bytes(tcp.payload))} bytes): {repr(bytes(tcp.payload)[:64])}")
        elif proto == 17 and UDP in packet:
            udp = packet[UDP]
            print(f"UDP: {udp.sport} -> {udp.dport}")
            if udp.payload:
                print(f"UDP Payload ({len(bytes(udp.payload))} bytes): {repr(bytes(udp.payload)[:64])}")
        elif proto == 1 and ICMP in packet:
            icmp = packet[ICMP]
            print(f"ICMP: Type {icmp.type} | Code {icmp.code}")
            if icmp.payload:
                print(f"ICMP Payload: {repr(bytes(icmp.payload)[:64])}")
        else:
            print(f"Other IP Protocol: {proto}")
            if ip.payload:
                print(f"IP Payload: {repr(bytes(ip.payload)[:64])}")
    else:
        print("Non-IP Packet detected.")
    print("="*80 + "\n")

def main():
    print("Expert Network Sniffer Started. Press Ctrl+C to stop.")
    scapy.sniff(prn=dissect_packet, store=False)

if __name__ == "__main__":
    main()
