def move_backward(client, x, s):
    from move_to import move_to
    
    print("Moving to x - ", x, " at ", s, "m/s")
    position = client.simGetGroundTruthKinematics()

    client.moveToPositionAsync(int(position.position.x_val)-int(x), int(position.position.y_val), int(position.position.z_val), int(s)).join()

    return 1;