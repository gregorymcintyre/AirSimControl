# control_sim.py
# Greg McIntye
# 7/11/2019
# simple console program to create and api interface
#

#!/usr/bin/env python3

import glob
import setup_path 
import airsim
from pathlib import Path
from move_to import move_to
from move_forward import move_forward

client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

print("\nCommand List\n--------------");
pyfiles = []
for file in glob.glob("*.py"):
    pyfiles.append(file[:-3])
    
pyfiles.remove('AirSimControl')
pyfiles.remove('test')
pyfiles.remove('setup_path')

print('\n'.join(pyfiles))
print('*q or quit')

state = True

while state:
    command = input("\nEnter Command: ")
    commandParse = command.split(" ");
    print(commandParse);

    if commandParse[0] == "move_to":
        move_to(client, commandParse[1],commandParse[2],commandParse[3],commandParse[4])
    elif commandParse[0] == "move_forward":
        move_forward(client, commandParse[1],commandParse[2])    
        
    elif command in pyfiles:
        exec(Path(str(command) + ".py").read_text())
    elif command == "*q" or command == "quit":
        client.enableApiControl(False);
        print("Exiting..")
        state = False
    else:
        print('Please enter a valid command')
