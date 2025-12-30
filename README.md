# Automated Network Auditor (v2.0)
**Turning Raw Network Data into Actionable Security Logs.**

## Overview
This particular python utility automates infrastructure reconnaissance by identifying open TCP ports on the targeted host. By design, it is made to assist in security auditing by providing time-stamped persistent logs of potential vulnerabilities.  

## Key Features
* **Automated Multi-Port Scan:** Iterates through a defined range (Ports 20–100) automatically.
* **Intelligent Logging:** Records only active ("Open") ports to eliminate data noise.
* **Real-Time Telemetry:** Captures and logs precise timestamps for every discovery.

## Technical Stack
* **Language:** Python 3
* **Core Library:** `socket` (Transport layer communication)
* **Utility:** `datetime` (Timed audit logging)

## Usage
1. Run the script: `python network_auditor.py`
2. Enter the target IP address when prompted.
3. Review results in `scan_result.txt`.

## Roadmap - Where it goes from here 
* Future integration with AI APIs to suggest mitigation strategies for discovered open ports.