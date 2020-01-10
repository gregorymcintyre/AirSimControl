def move_forward(client, x, s):
    from move_to import move_to
    
    print("Moving to x + ", x, " at ", s, "m/s")
    #print(client.simGetGroundTruthKinematics())
    position = client.simGetGroundTruthKinematics()
    
    #xValue = int(position.position.x_val)+int(x)
    #print(xValue)
    #yValue = int(position.position.y_val)
    #print(yValue)
    #zValue = int(position.position.z_val)
    #print(zValue)
    
    #client.moveToPositionAsync(xValue, yValue, zValue, int(s)).join()
    client.moveToPositionAsync(int(position.position.x_val)+int(x), int(position.position.y_val), int(position.position.z_val), int(s)).join()

    return 1;
    