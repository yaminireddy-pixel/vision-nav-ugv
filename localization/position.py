
def update_position(x, y, distance, heading_degrees):
    """
    Update estimated 2D position.
    Heading is measured in degrees from the positive x-axis.
    Distance is in meters.
    """
    import math

    heading = math.radians(heading_degrees)

    new_x = x + distance * math.cos(heading)
    new_y = y + distance * math.sin(heading)

    return new_x, new_y


if __name__ == "__main__":
    x = 0.0
    y = 0.0

    x, y = update_position(x, y, 2.0, 0.0)

    print("VISION-NAV Localization")
    print("Estimated X position:", round(x, 2), "meters")
    print("Estimated Y position:", round(y, 2), "meters")
