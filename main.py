import cv2
import csv
import os
from ultralytics import YOLO
from datetime import datetime

# ==============================
# LOAD YOLO MODEL
# ==============================
model = YOLO("yolo11n.pt")

# ==============================
# OPEN CCTV VIDEO
# ==============================
video = cv2.VideoCapture("border_post_cctv.mp4")

if not video.isOpened():
    print("ERROR: Could not open border_post_cctv.mp4")
    exit()

# ==============================
# VIRTUAL FENCE
# ==============================
LINE_Y = 350

# Store IDs that already generated an alert
alerted_ids = set()

# ==============================
# CREATE ALERT LOG
# ==============================
log_file = "alerts.csv"

if not os.path.exists(log_file):
    with open(log_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Date",
            "Time",
            "Camera",
            "Object",
            "Event",
            "Status"
        ])

print("IBVAP Surveillance System Started")

# ==============================
# MAIN LOOP
# ==============================
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

    # ==============================
    # DRAW VIRTUAL FENCE
    # ==============================

    cv2.line(
        frame,
        (0, LINE_Y),
        (frame.shape[1], LINE_Y),
        (0, 0, 255),
        3
    )

    cv2.putText(
        frame,
        "VIRTUAL FENCE - RESTRICTED AREA",
        (20, LINE_Y - 15),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2
    )

    # ==============================
    # DETECTION
    # ==============================

    boxes = results[0].boxes

    if boxes is not None:

        for box in boxes:

            class_id = int(box.cls[0])
            class_name = model.names[class_id]

            # Only monitor people
            if class_name != "person":
                continue

            # Tracking ID
            if box.id is None:
                continue

            track_id = int(box.id[0])

            # Bounding box
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Person center
            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)

            # Draw box
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            # Tracking ID
            cv2.putText(
                frame,
                f"Person #{track_id}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

            # ==============================
            # CHECK FENCE
            # ==============================

            if center_y > LINE_Y and track_id not in alerted_ids:

                alerted_ids.add(track_id)

                now = datetime.now()

                date = now.strftime("%Y-%m-%d")
                time = now.strftime("%H:%M:%S")

                # ==============================
                # SAVE EVENT
                # ==============================

                with open(log_file, "a", newline="") as file:

                    writer = csv.writer(file)

                    writer.writerow([
                        date,
                        time,
                        "BOP-01",
                        f"Person #{track_id}",
                        "Virtual Fence Intrusion",
                        "ALERT"
                    ])

                # ==============================
                # TERMINAL ALERT
                # ==============================

                print("\n================================")
                print("🚨 INTRUSION DETECTED")
                print("================================")
                print(f"Camera : BOP-01")
                print(f"Object : Person #{track_id}")
                print(f"Date   : {date}")
                print(f"Time   : {time}")
                print("Event  : Virtual Fence Intrusion")
                print("Status : ALERT")
                print("================================\n")

                # ==============================
                # VIDEO ALERT
                # ==============================

                cv2.putText(
                    frame,
                    "!!! INTRUSION DETECTED !!!",
                    (50, 70),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    3
                )

    # ==============================
    # IBVAP HEADER
    # ==============================

    cv2.putText(
        frame,
        "IBVAP - INTELLIGENT BORDER VIDEO ANALYTICS",
        (20, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "CAMERA: BOP-01 | STATUS: LIVE",
        (20, frame.shape[0] - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    # ==============================
    # DISPLAY
    # ==============================

    cv2.imshow(
        "IBVAP - Border Surveillance",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# ==============================
# CLEANUP
# ==============================

video.release()
cv2.destroyAllWindows()

print("\nIBVAP Surveillance System Stopped.")
print(f"Alert log saved to: {log_file}")