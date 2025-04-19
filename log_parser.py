import re
import os

# Regex patterns to detect common attack patterns
unauthorized_access_pattern = r"Failed password for .* from (\S+) port"
brute_force_pattern = r"Failed password for invalid user .* from (\S+) port"

def parse_logs(logfile):
    ip_addresses = {}

    with open(logfile, 'r') as file:
        for line in file:
            if re.search(unauthorized_access_pattern, line):
                ip = re.search(unauthorized_access_pattern, line).group(1)
                ip_addresses[ip] = ip_addresses.get(ip, 0) + 1

            if re.search(brute_force_pattern, line):
                ip = re.search(brute_force_pattern, line).group(1)
                ip_addresses[ip] = ip_addresses.get(ip, 0) + 1

    return ip_addresses

def highlight_anomalies(ip_addresses, threshold=5):
    for ip, count in ip_addresses.items():
        if count >= threshold:
            print(f"🚨 Anomaly detected from IP: {ip}, Attempted {count} times")

if __name__ == "__main__":
    log_file = "siem_log.txt"  # Replace with your log file
    ip_addresses = parse_logs(log_file)
    highlight_anomalies(ip_addresses)
