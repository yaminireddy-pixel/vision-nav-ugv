
def calculate_risk(distance, object_name):
    """
    Calculate a simple risk level based on distance.
    Distance is in meters.
    """

    if distance is None or distance <= 0:
        return "UNKNOWN"

    if distance <= 1.0:
        return "HIGH"

    elif distance <= 3.0:
        return "MEDIUM"

    else:
        return "LOW"


if __name__ == "__main__":
    test_distance = 0.5
    test_object = "person"

    risk = calculate_risk(test_distance, test_object)

    print("VISION-NAV Risk Mapping")
    print("Object:", test_object)
    print("Distance:", test_distance, "meters")
    print("Risk level:", risk)

