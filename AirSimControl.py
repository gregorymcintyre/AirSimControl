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
from move_backward import move_backward
from move_up import move_up
from move_down import move_down
from move_left import move_left
from move_right import move_right

client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

#client.drivetrain = airsim.DrivetrainType.ForwardOnly
#print("Fixed wing mode\n")

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
    elif commandParse[0] == "move_backward":
        move_backward(client, commandParse[1],commandParse[2]) 
    elif commandParse[0] == "move_up":
        move_up(client, commandParse[1],commandParse[2]) 
    elif commandParse[0] == "move_down":
        move_down(client, commandParse[1],commandParse[2]) 
    elif commandParse[0] == "move_left":
        move_left(client, commandParse[1],commandParse[2]) 
    elif commandParse[0] == "move_right":
        move_right(client, commandParse[1],commandParse[2]) 
        
    elif command in pyfiles:
        exec(Path(str(command) + ".py").read_text())
    elif command == "*q" or command == "quit":
        client.enableApiControl(False);
        print("Exiting..")
        state = False
    else:
        print('Please enter a valid command')
