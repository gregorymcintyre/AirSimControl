print("you found me!");

file = open("callsigns.txt", "r")
data = file.readlines()

state = True
collectedCallsign = []

while state:
    command = input("\nEnter Command: ")
    commandParse = command.split(" ");
    print(commandParse);
    
    #print(data)
    for line in data:
        words = line.split()
        #print(words)
        
        if words[0] == commandParse[1]:
            collectedCallsign = words
            print(commandParse[1])
            
    print(collectedCallsign)