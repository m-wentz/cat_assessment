import re

# Applicant: Michael Wentz
# Script to extract port numbers from Windows and Firewall logs
# NOTE: Assumes consistent log pattern for each index.

# Windows log sample
win_log = """
[redacted]
"""

# Firewall log sample
firewall_log = """
[redacted]
"""

# Regex patterns for extracting ports
win_port_pattern = r'Client Port: (\d+)'
firewall_port_pattern = r's_port:"(\d+)"'

# Extracting ports from logs and display
all_ports = re.findall(firewall_port_pattern, firewall_log) + \
    re.findall(win_port_pattern, win_log)
print("Ports Found: ", all_ports)
