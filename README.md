 CodeAlpha Basic Network Sniffer

 Project Overview
This project is a Python-based network packet sniffer developed as part of the CodeAlpha Cybersecurity Internship.

It uses the Scapy library to capture and analyze network packets on a selected network interface.

 Features
 Captures live network packets.
 Displays source and destination IP addresses.
 Identifies TCP, UDP and ICMP protocols.
 Displays source and destination port numbers.
 Displays a limited packet payload preview.
 Records packet timestamps.
 Counts captured packets.

 Technologies Used
 Python 3.13.14
 Scapy 2.7.0
 Kali Linux
 VirtualBox

 Project Structure
CodeAlpha_Basic_Network_Sniffer/
 sniffer.py
 sniffer_v2.py
 README.md

 Installation
Install Scapy if it is not already installed:
pip install scapy

 Usage
Run the original version:
sudo python3 sniffer.py

Run the improved version:
sudo python3 sniffer_v2.py

Press CTRL+C to stop packet capture.

 Testing
The sniffer was tested using authorized traffic generated from the Kali Linux virtual machine.

Tests included:
 ICMP traffic using ping.
 TCP traffic using curl.
 DNS traffic using nslookup.

 Learning Outcomes
This project provided practical experience in:
- Network packet capture.
- Understanding IP addressing.
- Identifying common network protocols.
- Examining packet headers and payloads.
- Using Python for basic network analysis.

 Ethical Considerations
This tool is intended for educational purposes and authorized network monitoring only. Packet capture should only be performed on networks where permission has been granted.

Adeniran Agnes Adedunmola — CodeAlpha Internship
