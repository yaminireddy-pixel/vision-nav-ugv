
from ultralytics import YOLO
import cv2


def estimate_distance(pixel_height, real_height, focal_length):
    if pixel_height <= 0:
        return None

    return (real_height * focal_length) / pixel_height


def main():
    model = YOLO("yolo11n.pt")
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not open camera.")
        return

    print("Live object detection started.")
    print("Press Q to stop.")

    while True:
        success, frame = camera.read()

        if not success:
            print("Error: Could not read camera frame.")
            break

        results = model.predict(source=frame, verbose=False)

        for box in results[0].boxes:
            pixel_height = float(box.xyxy[0][3] - box.xyxy[0][1])
            print(
                f"Object detected with height: "
                f"{pixel_height:.0f} pixels"
            )

        annotated_frame = results[0].plot()
        cv2.imshow("VISION-NAV Live Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

