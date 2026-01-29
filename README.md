# 🛡️ Cog-Link - AI-Powered Network Auditor

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Stable%20v2.0-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)

> A fast, AI-assisted network auditing tool that scans ports, analyzes risk, and generates professional security reports automatically.

------------------------------------------------------------------------

## 🌟 Highlights

-   ⚡ **Super fast** --- scans 1,000 ports in seconds using
    *multithreading*
-   🧠 **AI-powered insights** --- uses Google Gemini to explain risks & general safety measures,
    *not just list ports*
-   📄 **Auto-generated reports** --- clean Markdown reports with
    *timestamps*
-   🛡️ **Graceful & reliable** --- safe exits, error handling, and
    *modular architecture*
-   🔒 **Secure by design** --- API keys *isolated* via config files

------------------------------------------------------------------------

## ℹ️ Overview

**Cog-Link** is a multi-threaded network security auditor (port scanner). Built for people who want risk assessment and safety measures of the found open ports, all at one place. 

Most tools tell you *what* ports are open. List them out and leave it there.
Cog-Link goes some steps further and explains **what those open ports actually
mean & how to secure them** (risks & the saftey measures) using AI-powered analysis.

It combines: Traditional port scanning - Concurrent execution for
speed + Google Gemini 2.5 Flash for AI analysis + Automatic
Markdown reporting. 

Whether you're learner, developer or someone who wants to audit their own network infrastructure, Cog-Link is designed to be accessaccessible yet powerful for people with or without much experience.

------------------------------------------------------------------------

## 🚀 Usage

Run a scan by passing a target:

``` bash
python cog-link.py -t YOUR_TARGET_IP_ADDRESS
```

Example output:

``` plaintext
[*] Starting threaded scan on YOUR_TARGET_IP_ADDRESS...
[+] Found open port: 22
[+] Found open port: 80

[+] Sending 2 ports to AI Analyst...
[✔] Report successfully saved to: Audit_Report_2026-01-20.md
```

Each scan generates a professional report like:

    Audit_Report_YYYY-MM-DD.md

------------------------------------------------------------------------

## ⬇️ Installation

### Requirements

-   Python 3.11+
-   Works on Windows, Linux, and macOS


### Setup

Clone the repository:

``` bash
git clone https://github.com/YOUR_USERNAME/Cog-Link.git
cd Cog-Link
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

Configure your API key: 1. Rename `config_example.py` → `config.py`\
2. Add your Gemini API key:

``` python
API_KEY = "AIzaSyD..."
```

> `config.py` is git-ignored to protect your credentials.

------------------------------------------------------------------------

## 📂 Project Structure

``` plaintext
Cog-Link/
├── cog-link.py          # Main application logic
├── config.py            # API Key (Ignored by Git)
├── config_example.py    # Template for users
├── requirements.txt     # Dependency list
├── .gitignore           # Security rules
└── README.md            # Documentation
```

------------------------------------------------------------------------

## ⚠️ Disclaimer

This project is for **educational and ethical security research only**.\
You must have permission before scanning any network.\
The author is not responsible for misuse or damage caused by this tool.

------------------------------------------------------------------------

## 🤝 Contributing & Feedback

If you found this project cool/useful/interesting: 
- ⭐ Star the repo
- 🐛 Open an issue for bugs
- 💡 Suggest features
- 📣 Share feedback 

Your input is highly valued and encouraged.

------------------------------------------------------------------------

## 🙏 Collaboration 

I am open to collaborate for interesting projects. Just leave me an email @onlyshxcon@gmail.com
