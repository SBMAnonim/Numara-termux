#!/usr/bin/env python3

import os
os.system('clear')

import pyfiglet 
  
result = pyfiglet.figlet_format("Nomrebi.com") 
print(result)

import signal

def keyboardInterruptHandler(signal, frame):
    print("\nპროგრამა გაითიშა.".format(signal))
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

print("Nomrebi.com პარსერი")
print("---------------------------------------------------")
print("https://github.com/SBMAnonim")
print("---------------------------------------------------")

import requests
import re
params = {'number' : input(" kurbanin numarasini yazin telefon numarasi4: ")}

var = requests.post('https://simpleapi.info/apps/numbers-info/info.php?results=json', data = params)
found = re.search('"items":\[(.+?)\]', var.text).group(1)

print("--------------------------------------------------")