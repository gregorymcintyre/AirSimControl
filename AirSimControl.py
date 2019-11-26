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
import math


client = airsim.MultirotorClient()
client.confirmConnection()
#client.enableApiControl(True)
client.enableApiControl(True, "ALPHA")
client.enableApiControl(True, "BRAVO")
client.enableApiControl(True, "CHARLIE")
client.enableApiControl(True, "DELTA")
client.enableApiControl(True, "ECHO")
#client.armDisarm(True)
client.armDisarm(True, "ALPHA")
client.armDisarm(True, "BRAVO")
client.armDisarm(True, "CHARLIE")
client.armDisarm(True, "DELTA")
client.armDisarm(True, "ECHO")

#client.drivetrain = airsim.DrivetrainType.ForwardOnly
#print("Fixed wing mode\n")

print("\nCommand List\n-------------\n<ID> <CMD> <CS | Grid | (Polar & Alpha)> <S>\n");
print('land')
print('move_to')
print('takeoff')
print('quit')

file = open("callsigns.txt", "r")
data = file.readlines()

state = True
callsign = False
collectedCallsign = []
collectedCommand = []

while state:

    #print(dAlpha)
    #print(dBravo)
    
    command = input("\nEnter Command: ")
    commandParse = command.split(" ");
    #print(commandParse);
    
    if len(commandParse) == 1:
        collectedCommand = [0, commandParse[0]]
    elif len(commandParse) == 2:
        collectedCommand = [commandParse[0], commandParse[1]]
        
        
    elif commandParse[1] == "move_to":    
        if len(commandParse) == 3:
            print("<ID> <CMD> <CS>")
            #print("3: " + ' '.join(commandParse))
            for line in data:
                words = line.split()     
                if words[0] == commandParse[2]:
                    #print(words)
                    collectedCallsign = words
                    callsign = True
            collectedCommand = [commandParse[0], commandParse[1], collectedCallsign[1], collectedCallsign[2], collectedCallsign[3], 1]
            #print(collectedCommand)
        elif len(commandParse) == 4:
            print("<ID> <CMD> <CS> <S>")
            #print("4: " + ' '.join(commandParse))
            for line in data:
                words = line.split()     
                if words[0] == commandParse[2]:
                    #print(words)
                    collectedCallsign = words
                    callsign = True
            collectedCommand = [commandParse[0], commandParse[1], collectedCallsign[1], collectedCallsign[2], collectedCallsign[3], commandParse[3]]
            #print(collectedCommand)
        elif len(commandParse) == 5:
            print("<ID> <CMD> <X> <Y> <Z>")
            #print("5: " + ' '.join(commandParse))
            collectedCommand = [commandParse[0], commandParse[1], commandParse[2], commandParse[3], commandParse[4], 1]
            #print(collectedCommand)
        elif len(commandParse) == 6:
            print("<ID> <CMD> <X> <Y> <Z> <S>")
            #print("6: " + ' '.join(commandParse))
            collectedCommand = [commandParse[0], commandParse[1], commandParse[2], commandParse[3], commandParse[4], commandParse[5]]
            #print(collectedCommand)
        else:
            print('Move to, hu?')
            print('Please enter a valid command')
            
            
    elif commandParse[1] == "move_direction": 
        vx = math.sin(int(commandParse[2])*math.pi/180) + math.cos(int(commandParse[3])*math.pi/180)
        vy = math.sin(int(commandParse[2])*math.pi/180) + math.sin(int(commandParse[3])*math.pi/180)
        vz = math.cos(int(commandParse[2])*math.pi/180)
        
        if len(commandParse) == 4:
            print("<ID> <CMD> <POLAR> <ALPHA>")
            collectedCommand = [commandParse[0], commandParse[1], vx, vy, vz, -1]
        elif len(commandParse) == 5:
            print("<ID> <CMD> <POLAR> <ALPHA> <S | R>")
            collectedCommand = [commandParse[0], commandParse[1], vx, vy, vz, commandParse[4]]
        else:
            print('What direction?!')
            print('Please enter a valid command')
    
    #exec(Path("test.py").read_text())
    
    
    
    if len(collectedCommand) < 1:
        print("A boo boo has occured")
    elif collectedCommand[1] == "quit":
        print("Exiting...")
        client.armDisarm(True, "ALPHA")
        client.enableApiControl(False, "ALPHA")
        client.armDisarm(True, "BRAVO")
        client.enableApiControl(False, "BRAVO")
        client.armDisarm(True, "CHARLIE")
        client.enableApiControl(False, "CHARLIE")
        client.armDisarm(True, "DELTA")
        client.enableApiControl(False, "DELTA")
        client.armDisarm(True, "ECHO")
        client.enableApiControl(False, "ECHO")
        state = False
        quit();
    elif collectedCommand[1] == "getup":
        client.takeoffAsync(vehicle_name="ALPHA")
        client.takeoffAsync(vehicle_name="BRAVO")
        client.takeoffAsync(vehicle_name="CHARLIE")
        client.takeoffAsync(vehicle_name="DELTA")
        client.takeoffAsync(vehicle_name="ECHO")
    elif collectedCommand[1] == "getdown":
        client.landAsync(vehicle_name="ALPHA")
        client.landAsync(vehicle_name="BRAVO")
        client.landAsync(vehicle_name="CHARLIE")
        client.landAsync(vehicle_name="DELTA")
        client.landAsync(vehicle_name="ECHO")
    elif collectedCommand[1] == "starburst":
        client.moveToPositionAsync(0, 0, -10, 5, vehicle_name="ALPHA")
        client.moveToPositionAsync(10, 0, -1, 5, vehicle_name="BRAVO")
        client.moveToPositionAsync(0, 10, -1, 5, vehicle_name="CHARLIE")
        client.moveToPositionAsync(-10, 0, -1, 5, vehicle_name="DELTA")
        client.moveToPositionAsync(0, -10, -1, 5, vehicle_name="ECHO")
    elif collectedCommand[1] == "converge":
        client.moveToPositionAsync(0, 0, -1, 1, vehicle_name="ALPHA")
        client.moveToPositionAsync(0, 0, -1, 1, vehicle_name="BRAVO")
        client.moveToPositionAsync(0, 0, -1, 1, vehicle_name="CHARLIE")
        client.moveToPositionAsync(0, 0, -1, 1, vehicle_name="DELTA")
        client.moveToPositionAsync(0, 0, -1, 1, vehicle_name="ECHO")

        
    elif collectedCommand[1] == "move_to":
        print(collectedCommand)
        #print(collectedCommand[0], collectedCommand[1], collectedCommand[2], collectedCommand[3],collectedCommand[4],collectedCommand[5])
        #MultirotorRpcLibClient* MultirotorRpcLibClient::moveToPositionAsync(float x, float y, float z, float velocity, float timeout_sec, DrivetrainType drivetrain, const YawMode& yaw_mode, float lookahead, float adaptive_lookahead, const std::string& vehicle_name)
        client.moveToPositionAsync(int(collectedCommand[2]), int(collectedCommand[3]),int(collectedCommand[4]),int(collectedCommand[5]), vehicle_name=collectedCommand[0])
        #f1.join()
    elif collectedCommand[1] == "move_direction":
        print(collectedCommand)
        #MultirotorRpcLibClient* MultirotorRpcLibClient::moveByVelocityZAsync(float vx, float vy, float z, float duration, DrivetrainType drivetrain, const YawMode& yaw_mode, const std::string& vehicle_name)
        client.moveByVelocityZAsync(collectedCommand[2], collectedCommand[3], collectedCommand[4], int(collectedCommand[5]), vehicle_name=collectedCommand[0])
    elif collectedCommand[1] == "takeoff":
        landed = client.getMultirotorState(vehicle_name=collectedCommand[0]).landed_state
        if landed == airsim.LandedState.Landed:
            print("taking off...")
            client.enableApiControl(True, vehicle_name=collectedCommand[0])
            client.armDisarm(True, vehicle_name=collectedCommand[0])
            client.takeoffAsync(vehicle_name=collectedCommand[0]).join()
        else:
            print("already flying...")
            client.hoverAsync(vehicle_name=collectedCommand[0]).join()
    elif collectedCommand[1] == "land":
        landed = client.getMultirotorState(vehicle_name=collectedCommand[0]).landed_state
        if landed == airsim.LandedState.Landed:
            print("already landed...")
        else:
            print("landing...")
            client.landAsync(vehicle_name=collectedCommand[0]).join()
        client.armDisarm(False)
        client.enableApiControl(False)
    else:
        print('Please enter a valid command')

    
