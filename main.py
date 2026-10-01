import cv2
from ultralytics import YOLO

# Load the pretrained YOLO11 Nano model
# The model file will be downloaded automatically the first time
model = YOLO("yolo11n.pt")

# Open the default webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open webcam.")
    raise SystemExit

print("AI Object Detector is running!")
print("Press Q to quit.")

while True:
    # Read one frame from the webcam
    success, frame = cap.read()

    if not success:
        print("Could not read frame.")
        break

    # Run YOLO object detection
    results = model(frame, verbose=False)

    # Draw bounding boxes, labels and confidence scores
    annotated_frame = results[0].plot()

    # Display the result
    cv2.imshow("AI Object Detector", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()