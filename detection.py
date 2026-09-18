import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolo11n.pt")

# Open CCTV video
video = cv2.VideoCapture("border_post_cctv.mp4")

if not video.isOpened():
    print("ERROR: Could not open border_post_cctv.mp4")
    exit()

while True:
    ret, frame = video.read()

    if not ret:
        break

    # YOLO tracking
    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        verbose=False
    )

    # Draw boxes + tracking IDs
    annotated_frame = results[0].plot()

    cv2.imshow("IBVAP - AI Border Surveillance", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()