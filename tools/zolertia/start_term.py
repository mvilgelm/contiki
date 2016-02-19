#!/usr/bin/python

import os
import re
import subprocess


home = os.getenv("HOME")
workdir = home+'/Projects/TSCH/github/contiki/tools/zolertia'

output = subprocess.check_output(workdir+'/motelist-zolertia').decode("utf-8")

# print(output)

lines = output.splitlines()

# print(len(output.split('\n')))

devices = [re.findall('/dev/ttyUSB.', line)[0] for line in lines if "Z1" in line]

print(devices)

if len(devices)==0:
    print('no devices present')
else:
    for dev in devices:
        os.system('gtkterm --port=%s --speed=115200 &' % dev)
