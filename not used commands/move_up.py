def move_up(client, z, s):
    from move_to import move_to
    
    print("Moving to z - ", z, " at ", s, "m/s")
    position = client.simGetGroundTruthKinematics()

    client.moveToPositionAsync(int(position.position.x_val), int(position.position.y_val), int(position.position.z_val)-int(z), int(s)).join()

    return 1;