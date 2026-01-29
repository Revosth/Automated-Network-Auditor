"""
GOAL : Automate detection of open ports, risk analysis & suggest safety relevant safety measures report generation
PROJECT: Cog-link Automated Network Auditor (v2.0)
NETWORK LAYER: Operating at OSI layer 4 (Transport) using TCP Handshake logic.
MODEL: gemini-2.5-flash
"""

import socket
import datetime
import argparse
import sys
from concurrent.futures import ThreadPoolExecutor , as_completed

try:
    import config
    from google import genai
except ImportError:
    print("[!] Error: 'config.py' not found or 'google-genai' missing.")
    print("    Please ensure you have a 'config.py' file with 'API_KEY = ...'")
    print("    and installed requirements via 'pip install -r requirements.txt'")
    sys.exit(1)

def save_to_markdown(ip_address, open_ports, response_content): #Function to save report as .md file
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"Audit_Report_{timestamp}.md"

    report_content = f"""Automated Network Security Report:
**Target:** {ip_address} |
**Scan Date:** {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

---

##  ~Raw Findings **Open Ports Detected:**
```json
{open_ports}
```


{response_content}"""

    try:
      with open(filename, "w", encoding="utf-8") as f:
        f.write(report_content)
        print(f"\n[✔] Report successfully saved to: {filename}")
    except Exception as e:
       print(f"\n[X] Error while saving report: {e}")

def scan_port(ip, port): # Worker function to check a single TCP port. Returns the port number if open, None otherwise.

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)

            result = s.connect_ex((ip, port))


            if result == 0:
                return port
    except socket.timeout:
        return None
    except ConnectionRefusedError:
        return None
    except Exception: # Pass on generic errors to keep CLI output clean during threading
        return None


def generate_security_report(port_list, scanned_ip): #Sends open port data to Google Gemini for report generation.

    if not port_list:
        print("\nNo open ports found. No need for a Report.")
        return
    print(f"\n[+] Sending {len(port_list)} ports to AI Analyst...")

    try:
        client = genai.Client(api_key=config.API_KEY)

        prompt = f"""
    I have scanned a network and found these open ports: {port_list}.
    Act as a Senior Cybersecurity Analyst. 
    For each port, explain:
    1. What service usually runs on it.
    2. The potential security risks.
    3. How to secure it.
    Keep it concise and professional.
    """

        response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
        )


        save_to_markdown(scanned_ip, port_list, response.text)

    except Exception as e:
        print(f"\n[X]AI Analysis Failed: {e}")
        # Fallback: Save just the raw data if AI fails
        save_to_markdown(scanned_ip, port_list, "**[!]AI Analysis Unavailable (API ERROR)**")

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description = "Cog-Link: Automated Network Auditor v2.0")
    parser.add_argument('-t', '--target', required = True , help = "Target IP address")
    args = parser.parse_args()
    target_ip = args.target

#Standard System Ports 1-1000
target_port = range(1,1001)
found_open = []

print(f"[*] Starting multi-threaded scan on {target_ip}...")

with ThreadPoolExecutor(max_workers=100) as executor:
    # Launch all tasks
    futures = [executor.submit(scan_port,  target_ip , port) for port in target_port]

    try:
        # Process results as they arrive
        for future in as_completed(futures):
            result_port = future.result()
            if result_port is not None:
                print(f"\n[+] Found open port: {result_port}")
                found_open.append(result_port)

    except KeyboardInterrupt:
         print(f"\n[*] Cancelling scan on {target_ip}: interrupted by user.")
         executor.shutdown(wait=False , cancel_futures=True)

         if found_open:
             print(f"[*] Saving partial findings for {len(found_open)} ports...")
             save_to_markdown(
                 target_ip,
                 found_open,
"**[!] SCAN INTERRUPTED**\nAI Analysis was skipped because the user cancelled the scan."
             )
         else:
             print("[*] No open ports found yet. Exiting.")
         sys.exit(0)

# Proceed to AI analysis if scan finishes normally
generate_security_report(found_open , target_ip)