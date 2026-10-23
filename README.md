# VISION-NAV: Vision-Based Autonomous Navigation for UGV

## Project Overview
VISION-NAV is a prototype for vision-based autonomous navigation of an Unmanned Ground Vehicle (UGV) in outdoor environments. It combines object detection, risk mapping, path-planning decisions, vehicle-control commands, and vehicle simulation.

## Features
- Object detection using YOLO and OpenCV.
- Live camera detection.
- Risk classification based on obstacle distance.
- Navigation decisions: STOP, SLOW DOWN, and CONTINUE.
- Simulated vehicle control and movement.

## Project Structure
- `perception/` — Object detection and live camera processing.
- `risk_mapping/` — Obstacle risk classification.
- `planning/` — Navigation action selection.
- `localization/` — Basic position updates.
- `control/` — Simulated vehicle-control commands.
- `simulation/` — Vehicle movement simulation.
- `main.py` — Main program.

## Current Status
The prototype runs locally and has been tested with manually supplied distances for HIGH, MEDIUM, and LOW risk scenarios.

## Future Improvements
- Estimate obstacle distances using calibrated camera measurements.
- Integrate perception outputs with risk mapping.
- Improve localization and path planning.
- Evaluate performance in outdoor test environments.

## Disclaimer
This is a prototype for development and simulation. It has not been validated for safe autonomous operation of a real vehicle.
