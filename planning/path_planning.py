
def choose_action(risk_level):
    """
    Choose a basic navigation action based on obstacle risk.
    """

    if risk_level == "HIGH":
        return "STOP"

    elif risk_level == "MEDIUM":
        return "SLOW DOWN"

    elif risk_level == "LOW":
        return "CONTINUE"

    else:
        return "STOP - UNKNOWN RISK"


if __name__ == "__main__":
    print("VISION-NAV Path Planning")

    test_risks = ["HIGH", "MEDIUM", "LOW", "UNKNOWN"]

    for risk in test_risks:
        action = choose_action(risk)
        print("Risk:", risk, "-> Action:", action)
