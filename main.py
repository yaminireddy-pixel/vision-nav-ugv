
from risk_mapping.risk_map import calculate_risk
from planning.path_planning import choose_action
from control.vehicle_control import control_vehicle
from simulation.vehicle_simulation import simulate_vehicle


def main():
    print("=== VISION-NAV Autonomous Navigation ===")

    object_name = "person"
    distance = 2.0

    risk_level = calculate_risk(distance, object_name)
    action = choose_action(risk_level)
    speed, steering = control_vehicle(action)
    simulate_vehicle(speed, 5)

    print("Object:", object_name)
    print("Distance:", distance, "meters")
    print("Risk level:", risk_level)
    print("Navigation action:", action)
    print("Speed command:", speed)
    print("Steering command:", steering)


if __name__ == "__main__":
    main()
