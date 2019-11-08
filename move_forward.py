def move_forward(client, x, s):
    from move_to import move_to
    
    print("Moving to x + ", x, " at ", s, "m/s")
    #print(client.simGetGroundTruthKinematics())
    position = client.simGetGroundTruthKinematics()
    print(str(position.position.x_val), " = ", str((position.position.x_val)+float(x)))
    client.moveToPositionAsync(int((position.position.x_val)+float(x)), int(position.position.y_val), int(position.position.z_val), s).join()

    #values just not getting in?!

    return 1