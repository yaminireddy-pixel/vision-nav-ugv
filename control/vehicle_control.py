
def control_vehicle(action):
    """
    Convert a navigation decision into simulated vehicle commands.
    This does not control real hardware.
    """

    if action == "STOP":
        speed = 0.0
        steering = 0.0

    elif action == "SLOW DOWN":
        speed = 0.5
        steering = 0.0

    elif action == "CONTINUE":
        speed = 1.0
        steering = 0.0

    else:
        speed = 0.0
        steering = 0.0
        action = "STOP - UNKNOWN COMMAND"

    return speed, steering, action


if __name__ == "__main__":
    print("VISION-NAV Vehicle Control")

    test_actions = ["STOP", "SLOW DOWN", "CONTINUE"]

    for action in test_actions:
        speed, steering, command = control_vehicle(action)

        print(
            f"Action: {command} | "
            f"Speed command: {speed} | "
            f"Steering command: {steering}"
        )
