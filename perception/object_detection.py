
from ultralytics import YOLO


def detect_objects(image_path):
    # Load the YOLO11n model
    model = YOLO("yolo11n.pt")

    # Detect objects in the input image
    results = model.predict(source=image_path, save=True)

    # Display detected object names
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            object_name = model.names[class_id]
            confidence = float(box.conf[0])

            print(
                f"Detected: {object_name}, "
                f"Confidence: {confidence:.2f}"
            )


if __name__ == "__main__":
    detect_objects("https://ultralytics.com/images/bus.jpg")
