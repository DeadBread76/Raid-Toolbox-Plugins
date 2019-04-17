# Plugin Author: DeadBread76
# Plugin Name: Random User Ping spammer
# Date: 03/04/2019

import subprocess
import time
import sys
import os

pyprefix = sys.argv[1]
SERVER = input("Server ID: ")
tokenlist = open("tokens.txt").read().splitlines()
for token in tokenlist:
    p = subprocess.Popen([pyprefix,'plugins/Random Member Ping Spammer/randomuserping.py',token,SERVER],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    time.sleep(0.1)
    with open('pluginpids', 'a+') as handle:
        handle.write(str(p.pid)+'\n')
input("Press enter to return to raid toolbox.")
