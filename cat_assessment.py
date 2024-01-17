import re

# Applicant: Michael Wentz
# Script to extract port numbers from Password, Windows and Firewall logs
# NOTE: Assumes consistent log pattern for each index.

# Failed password log sample
pass_log = """
[redacted]
"""

# Windows log sample
win_log = """
[redacted]
"""

# Firewall log sample
firewall_log = """
[redacted]
"""

# Regex patterns for extracting ports
pass_log_pattern = r'port (\d+)'
win_port_pattern = r'Client Port: (\d+)'
firewall_port_pattern_1 = r's_port:"(\d+)"'
firewall_port_pattern_2 = r'service:"(\d+)"'

# Extracting ports from logs and display
all_ports = re.findall(pass_log_pattern, pass_log) + \
    re.findall(win_port_pattern, win_log) + \
    re.findall(firewall_port_pattern_1, firewall_log) + \
    re.findall(firewall_port_pattern_2, firewall_log)
print("Ports Found: ", all_ports)
