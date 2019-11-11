def move_left(client, y, s):
    from move_to import move_to
    
    print("Moving to y - ", y, " at ", s, "m/s")
    position = client.simGetGroundTruthKinematics()

    client.moveToPositionAsync(int(position.position.x_val), int(position.position.y_val)-int(y), int(position.position.z_val), int(s)).join()

    return 1;