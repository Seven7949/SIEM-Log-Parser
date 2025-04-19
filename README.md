# SIEM-Log-Parser
“Automated log parser for SIEM, detects anomalies like unauthorized access and brute-force attacks.”


# SIEM Log Analysis Automation Tool 🛠️

## Overview
This Python tool is designed to automatically parse SIEM logs, filter, and highlight anomalies such as unauthorized access attempts and brute-force login patterns. 

## Features
- **Parses SIEM log files**: Looks for failed login attempts, unauthorized access, and brute-force patterns.
- **Highlights suspicious activity**: Anomalies are flagged if a threshold (default: 5 attempts) is exceeded.
- **Customizable**: Add or modify detection patterns easily.

## Requirements
- Python 3.7+
- Regular Expressions

## Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/SIEM-Log-Parser.git
    cd SIEM-Log-Parser
    ```

2. Run the tool:
    ```bash
    python3 log_parser.py
    ```

> **Important:** Ensure you have your SIEM logs (e.g., `siem_log.txt`) in the same directory, or modify the script to point to the correct log location.

## License
MIT License (Choose an appropriate license if necessary)
