"""
PROJECT: Automated Network Auditor (v2.0)
PURPOSE: Performs automated TCP port discovery and logs open ports for security auditing.
"""

import socket
import datetime

target_ip = input("Please enter the target IP address: ")

# --- NETWORK SENSOR CONFIGURATION ---
for port in range(20, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializing the socket and set connection parameters.
    s.settimeout(0.5) # Using a 0.5s timeout to ensure the scan is fast enough for a multi-port range
    result= s.connect_ex((target_ip, port)) # Returns 0 if connection is successful (Port Open)

    if result == 0:
        nowt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Logic: Only open the file in 'append' mode to prevent overwriting previous discovery logs.
        with open("scan_result.txt", "a") as log:
            log.write(f"{nowt}: Port {port} of IP {target_ip} is OPEN. \n")
        print(f"Port {port} is OPEN. \n")
    s.close()