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
#client.enableApiControl(True)
client.enableApiControl(True, "Drone1")
client.enableApiControl(True, "Drone2")
#client.armDisarm(True)
client.armDisarm(True, "Drone1")
client.armDisarm(True, "Drone2")

#client.drivetrain = airsim.DrivetrainType.ForwardOnly
#print("Fixed wing mode\n")

dAlpha = client.takeoffAsync(vehicle_name="ALPHA")
dBravo = client.takeoffAsync(vehicle_name="BRAVO")
dAlpha.join()
dBravo.join()

print("\nCommand List\n--------------");
pyfiles = []
for file in glob.glob("*.py"):
    pyfiles.append(file[:-3])
    
pyfiles.remove('AirSimControl')
pyfiles.remove('test')
pyfiles.remove('setup_path')

print('\n'.join(pyfiles))
print('*q or quit')

file = open("callsigns.txt", "r")
data = file.readlines()


state = True
callsign = False
collectedCallsign = []

while state:
    command = input("\nEnter Command: ")
    commandParse = command.split(" ");
    print(commandParse);
    #if len(commandParse) == 
    
    #print(data)
    for line in data:
        words = line.split()
        #print(words)
        
        try:
            if words[0] == commandParse[1]:
                #print(commandParse[1])
                collectedCallsign = words
                callsign = True
                print(collectedCallsign)
        except:
            print("", end="")
    
    if commandParse[0] == "move_to":
        if callsign:
            move_to(client, collectedCallsign[1], collectedCallsign[2], collectedCallsign[3], commandParse[2])
            #print(client, commandParse[1], collectedCallsign[1], collectedCallsign[2],collectedCallsign[3])
            callsign = False
        else:
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
