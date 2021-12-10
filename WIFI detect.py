import subprocess

#    Import the re module so we can make use of regular expressions.
import re

command_output = subprocess.run(["netsh", "wlan", "show", "network", ], capture_output=True).stdout.decode()
print(command_output)

network_names = (re.findall("SSID (.*)\r", command_output))
print(network_names)
