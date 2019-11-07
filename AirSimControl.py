# control_sim.py
# Greg McIntye
# 7/11/2019
# simple console program to create and api interface
#

#!/usr/bin/env python3

import glob
from pathlib import Path

print("\nCommand List\n--------------");
pyfiles = []
for file in glob.glob("*.py"):
    pyfiles.append(file[:-3])
    
pyfiles.remove('AirSimControl')
pyfiles.remove('test')
pyfiles.remove('setup_path')

print('\n'.join(pyfiles))
print('*q or quit')

while True:
    command = input("\nEnter Command: ")
    
    if command in pyfiles:
        exec(Path(str(command) + ".py").read_text())
    elif command == '*q' or 'quit':
       #client.enableApiControl(False);
       quit();
    else:
        print('Please enter a valid command')
