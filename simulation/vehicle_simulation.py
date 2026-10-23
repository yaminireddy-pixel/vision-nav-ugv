
def simulate_vehicle(speed, duration):
    """
    Simulate a vehicle moving in a straight line.
    Speed is in meters per second.
    Duration is in seconds.
    """

    distance = speed * duration

    print("VISION-NAV Vehicle Simulation")
    print("Speed:", speed, "m/s")
    print("Duration:", duration, "seconds")
    print("Distance travelled:", distance, "meters")


if __name__ == "__main__":
    simulate_vehicle(speed=1.0, duration=5)
