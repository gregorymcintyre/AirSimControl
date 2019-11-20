# RandomGrid.py
# Greg McIntye
# 18/11/2019
# creates a random grid because im lazy
#

def RandomGrid(): 
    import random

    location = []

    location.append(random.randint(-10, 10))
    #x
    location.append(random.randint(-10, 10))
    #y
    location.append(random.randint(0, 10))
    #z

    print(location)
    return location;
    
    
for x in range(26):
    RandomGrid()