import subprocess
import sys
import os

pyprefix = sys.argv[1]
tokenlist = open("tokens.txt").read().splitlines()
if len(tokenlist) == 1:
    master = input("Who am I copying? (ID): ")
    print("Okie Dokie! I will copy this user now.")
else:
    master = input("Who are we copying? (ID): ")
    print("Okie Dokie! We will copy this user now.")
for token in tokenlist:
    p = subprocess.Popen([pyprefix,'plugins/Mimic/mimic.py',token,master],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    with open('pluginpids', 'a+') as handle:
        handle.write(str(p.pid)+'\n')
input("Press enter to return to raid toolbox.")
