# Malicious IP Blocker

[![MIT License](https://img.shields.io/badge/license-MIT-blue)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/downloads/)

## Description

**Malicious IP Blocker** is a Python script that automates the process of hardening your Windows Defender Firewall. It retrieves an updated list of known malicious IP addresses from [Feodo Tracker’s IP blocklist](https://feodotracker.abuse.ch/) and then reconfigures the firewall to block both inbound and outbound traffic from those IPs.

This script is ideal for system administrators and security enthusiasts who want a straightforward, automated method to protect their Windows systems from known malicious entities.

---

## Features

### Firewall Rule Management

- **Clean-Up:**  
  Before applying new rules, any pre-existing firewall rules named `Malicious` are removed to prevent conflicts.

- **Bidirectional Blocking:**  
  New rules are added to block both inbound and outbound traffic for each malicious IP.

### Automated IP List Retrieval

- **Real-Time Updates:**  
  Downloads the latest CSV file from Feodo Tracker, ensuring your block list is always up-to-date.

### Cross-Protocol Blocking

- **Comprehensive Protection:**  
  Blocks traffic regardless of protocol (TCP, UDP, etc.), securing your system from multiple attack vectors.

### Logging & Visibility

- **Console Feedback:**  
  Displays progress messages in the terminal, so you know which IPs have been blocked and when rules are added.

---

## Requirements

- **Operating System:** Windows (the script uses `netsh advfirewall` commands).
- **Python Version:** 3.x

### Python Libraries

- **`requests`** — Used to fetch the IP blocklist.  
- **`csv`** — Utilized for parsing the CSV file *(part of Python’s standard library)*.  
- **`subprocess`** — Executes firewall commands *(part of Python’s standard library)*.

To install the required third-party library, run:

```bash
pip install requests
```

### Note: You must run this script with administrative privileges to modify Windows Defender Firewall rules (e.g., by running the Command Prompt as an Administrator).

- **Author**: Zaniar Karimi

## License

This project is licensed under the MIT License. See below for details:

---

**MIT License**

Copyright (c) 2023 Zaniar Karimi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---
