# Plugin Author: DeadBread76
# Plugin Name: Random User Ping spammer
# Date: 03/04/2019

import subprocess
import time
import sys
import os
SERVER = input("Server ID: ")
tokenlist = open("tokens.txt").read().splitlines()
for token in tokenlist:
    if sys.platform.startswith('win32'):
        p = subprocess.Popen(['python','.\\plugins\\randomuserping.py',token,SERVER],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    elif sys.platform.startswith('linux'):
        p = subprocess.Popen(['python','plugins/randomuserping.py',token,SERVER],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    time.sleep(0.1)
    with open('pluginpids', 'a+') as handle:
        handle.write(str(p.pid)+'\n')
input("Press enter to return to raid toolbox.")
