# Basic Network Sniffer

A Python-based network sniffer for capturing and analyzing network traffic packets. This tool helps you understand how data flows through a network, the structure of packets, and the basics of networking protocols.

## Features

- **Packet Capture:** Capture live network traffic using Python.
- **Packet Analysis:** Parse and display packet details such as source/destination IP addresses, protocols, and payloads.
- **Protocol Insights:** Understand the basics of protocols by inspecting real traffic.
- **Extensible:** Built with Python libraries such as `scapy` or `socket` for flexibility and extensibility.

## Requirements

- Python 3.6 or higher
- [scapy](https://scapy.net/) (Recommended)
- Administrator/root privileges (for packet capturing)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. **Install dependencies:**
   ```bash
   pip install scapy
   ```

## Usage

> **Note:** You may need superuser privileges to capture packets (use `sudo` on Linux/macOS).

### Run the sniffer

```bash
sudo python sniffer.py
```

### Example Output

```
[+] Captured Packet: Protocol=TCP
    Source IP: 192.168.1.10
    Destination IP: 142.250.190.142
    Payload: GET / HTTP/1.1...
```

## How It Works

- The program uses `scapy` (or optionally `socket`) to capture packets on a network interface.
- For each packet, it extracts and displays:
  - Source IP address
  - Destination IP address
  - Protocol type (TCP, UDP, ICMP, etc.)
  - Raw payload data

## Learning Objectives

- Understand network packet structure and protocol basics.
- Gain hands-on experience with packet capturing tools in Python.
- Explore real network data flows.

## Extending the Project

- Add filters for specific protocols or ports.
- Save captured packets to a file (e.g., pcap format).
- Analyze and visualize traffic statistics.

## License

MIT License

## Disclaimer

This tool is for educational purposes only. Do not use it to capture network traffic without proper authorization.
