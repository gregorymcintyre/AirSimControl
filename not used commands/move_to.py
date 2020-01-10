
def move_to (client, x, y, z, s):
    print("Moving to (", x, " ", y, " ", z, ") at ", s, "m/s")

    client.moveToPositionAsync(int(x), int(y), int(z), int(s)).join()
    #client.moveToPositionAsync(-10, 10, -10, 5).join()
    client.hoverAsync().join()

    return 1