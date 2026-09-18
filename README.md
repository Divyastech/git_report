# IBVAP – Intelligent Border Video Analytics Platform

## AI-Powered CCTV Analytics for Border Security

**IBVAP (Intelligent Border Video Analytics Platform)** is a software-based AI and Computer Vision system designed to enhance surveillance at border locations using existing CCTV/IP camera infrastructure.

The platform aims to reduce the dependency on continuous manual CCTV monitoring by automatically detecting people and vehicles, tracking their movement, identifying virtual-fence violations, generating intrusion alerts, and maintaining an event log.

> **Current Status:** Prototype – approximately 40% implementation
> **Current working modules:** CCTV video input, object detection, object tracking, virtual-fence intrusion detection, real-time alerts, and event logging.

---

## 1. Problem Statement

Border security forces use CCTV cameras at Border Out Posts (BOPs), check posts, border roads, and other strategic locations.

Traditional CCTV systems primarily provide video recording or live streaming. Continuous monitoring requires personnel to observe multiple camera feeds, which can make it difficult to identify important events quickly.

Advanced surveillance capabilities such as:

* Face Recognition Systems (FRS)
* Automatic Number Plate Recognition (ANPR)
* Human and vehicle tracking
* Intrusion detection
* Suspicious activity detection
* Night-time movement detection

may require specialized systems or additional infrastructure.

The proposed IBVAP platform focuses on providing AI-based video analytics through software that can work with standard CCTV video streams.

---

# 2. Proposed Solution

IBVAP processes CCTV video using Artificial Intelligence and Computer Vision techniques.

The current prototype follows this pipeline:

```text
CCTV Video
     ↓
Video Frame Processing
     ↓
YOLO Object Detection
     ↓
Object Tracking
     ↓
Virtual Fence Detection
     ↓
Intrusion Alert
     ↓
Event Logging
```

The system analyzes video frames and identifies relevant objects such as people and vehicles.

Detected objects are assigned tracking IDs so that their movement can be monitored across consecutive frames.

A virtual boundary is defined within the surveillance area. When a tracked person crosses the boundary, the system generates an intrusion alert and records the event.

---

# 3. Objectives

The major objectives of IBVAP are:

1. To analyze CCTV video using Artificial Intelligence.
2. To automatically detect people and vehicles.
3. To track detected objects across video frames.
4. To identify unauthorized movement across a predefined virtual boundary.
5. To generate real-time intrusion alerts.
6. To automatically maintain a security event log.
7. To reduce dependency on continuous manual monitoring.
8. To provide a foundation for future advanced surveillance capabilities.

---

# 4. Current Prototype Implementation

The current prototype implements the core surveillance pipeline.

### Implemented Features

### 4.1 CCTV Video Input

The system accepts a CCTV video file as input.

Example:

```text
CCTV.mp4
```

OpenCV is used to read and process the video frame by frame.

---

### 4.2 Person and Vehicle Detection

The prototype uses the YOLO object detection model to identify objects in CCTV footage.

Current detection includes objects such as:

* Person
* Car
* Motorcycle
* Bus
* Truck

The detected objects are displayed using bounding boxes.

Example:

```text
┌──────────────────────────────┐
│                              │
│     ┌────────────┐           │
│     │   PERSON   │           │
│     │   #1       │           │
│     └────────────┘           │
│                              │
│            ┌────────────┐    │
│            │  VEHICLE   │    │
│            │    #2      │    │
│            └────────────┘    │
│                              │
└──────────────────────────────┘
```

---

### 4.3 Object Tracking

Object tracking is implemented using ByteTrack through the Ultralytics tracking framework.

Each detected object receives a unique tracking ID.

For example:

```text
Person #1
Person #2
Vehicle #3
```

This allows the system to distinguish between different objects and monitor their movement.

The tracking functionality uses persistent IDs between video frames.

---

### 4.4 Virtual Fence

A virtual boundary is created inside the CCTV frame.

Example:

```text
--------------------------------
       VIRTUAL FENCE
--------------------------------
```

The system continuously monitors tracked objects relative to this boundary.

When a tracked person crosses the virtual fence, the system identifies the event as a potential intrusion.

---

### 4.5 Intrusion Detection

When a tracked object crosses the predefined virtual boundary, the system generates an intrusion alert.

Example:

```text
!!! INTRUSION DETECTED !!!
```

The alert contains information such as:

* Camera ID
* Object ID
* Object type
* Date
* Time
* Event type
* Status

Example:

```text
Camera: BOP-01
Object: Person #1
Event: Virtual Fence Intrusion
Status: ALERT
```

---

### 4.6 Event Logging

Detected security events are stored in a CSV file.

Current log file:

```text
alerts.csv
```

Example structure:

| Date       | Time     | Camera | Object    | Event                   | Status |
| ---------- | -------- | ------ | --------- | ----------------------- | ------ |
| 2026-09-18 | 10:32:15 | BOP-01 | Person #1 | Virtual Fence Intrusion | ALERT  |

This provides a simple audit trail of detected security events.

---

# 5. Technology Stack

## Programming Language

**Python**

Python is used for video processing, AI model execution, tracking, and event logging.

## Computer Vision

**OpenCV**

Used for:

* Reading CCTV video
* Processing video frames
* Displaying detection results
* Drawing bounding boxes
* Drawing virtual boundaries
* Displaying alerts

## Object Detection

**YOLO**

YOLO is used for real-time object detection in CCTV footage.

The current prototype uses:

```text
YOLO11n
```

## Object Tracking

**ByteTrack**

Used to maintain object identities across video frames.

## Data Logging

**CSV / Pandas**

Security events are stored and processed using CSV-based logging.

## Development Environment

* Python
* VS Code
* Windows
* Ultralytics
* OpenCV
* Pandas

---

# 6. System Architecture

The current prototype architecture can be represented as:

```text
             CCTV CAMERA / VIDEO
                     │
                     ▼
              Video Acquisition
                     │
                     ▼
              OpenCV Processing
                     │
                     ▼
              YOLO Detection
                     │
             ┌───────┴───────┐
             ▼               ▼
          Person           Vehicle
             │               │
             └───────┬───────┘
                     ▼
                ByteTrack
                     │
                     ▼
              Object Tracking
                     │
                     ▼
              Virtual Fence
                     │
              ┌──────┴──────┐
              │             │
           No Event       Crossing
                            │
                            ▼
                    Intrusion Alert
                            │
                            ▼
                       alerts.csv
```

---

# 7. Working Methodology

## Step 1 – Capture CCTV Input

The system receives CCTV video input.

```text
CCTV.mp4
```

The video is read frame by frame using OpenCV.

## Step 2 – Detect Objects

Each frame is passed to the YOLO model.

The model identifies objects and generates bounding boxes.

## Step 3 – Track Objects

The detected objects are passed through the tracking system.

Each object receives a tracking ID.

## Step 4 – Monitor Virtual Boundary

A predefined virtual line is placed in the surveillance area.

The system checks the position of tracked objects relative to the line.

## Step 5 – Detect Intrusion

If an object crosses the virtual boundary, the system triggers an intrusion event.

## Step 6 – Generate Alert

The system displays:

```text
!!! INTRUSION DETECTED !!!
```

## Step 7 – Store Event

The event is recorded in:

```text
alerts.csv
```

This creates a basic digital security event history.

---

# 8. Project Folder Structure

The current prototype can be organized as:

```text
IBVAP/
│
├── main.py
├── CCTV.mp4
├── yolo11n.pt
├── alerts.csv
├── dashboard.py
└── README.md
```

### File Description

| File           | Purpose                              |
| -------------- | ------------------------------------ |
| `main.py`      | Main AI/CCTV processing program      |
| `CCTV.mp4`     | Sample CCTV input                    |
| `yolo11n.pt`   | YOLO object detection model          |
| `alerts.csv`   | Generated security event log         |
| `dashboard.py` | Streamlit-based monitoring dashboard |
| `README.md`    | Project documentation                |

---

# 9. Running the Project

## Step 1 – Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Move into the project directory:

```bash
cd IBVAP
```

---

## Step 2 – Install Dependencies

Install the required Python packages:

```bash
pip install ultralytics opencv-python pandas numpy
```

If Streamlit is being used:

```bash
pip install streamlit
```

---

## Step 3 – Run the AI Prototype

Run:

```bash
python main.py
```

The CCTV video will open and the system will start detecting and tracking objects.

---

## Step 4 – Test Intrusion Detection

When a tracked person crosses the virtual fence, the system displays:

```text
!!! INTRUSION DETECTED !!!
```

The event is also stored in:

```text
alerts.csv
```

---

# 10. Example Output

The prototype produces an annotated CCTV feed containing:

```text
Camera: BOP-01

Person #1
Person #2
Vehicle #3

-------------------------------
       VIRTUAL FENCE
-------------------------------

!!! INTRUSION DETECTED !!!
```

The corresponding event is stored in the security log.

---

# 11. Dashboard

A Streamlit-based dashboard is being developed to provide a centralized interface for monitoring the surveillance system.

The dashboard is intended to provide:

* CCTV monitoring
* Security event logs
* Intrusion information
* AI analytics
* Camera information
* Event statistics

The dashboard provides a foundation for future integration with multiple CCTV cameras and advanced analytics.

---

# 12. Current Implementation Status

The project is currently under active development.

| Module                        | Status                   |
| ----------------------------- | ------------------------ |
| CCTV video input              | ✅ Implemented            |
| Video frame processing        | ✅ Implemented            |
| YOLO object detection         | ✅ Implemented            |
| Person detection              | ✅ Implemented            |
| Vehicle detection             | ✅ Implemented            |
| Object tracking               | ✅ Implemented            |
| Virtual fence                 | ✅ Implemented            |
| Intrusion detection           | ✅ Implemented            |
| Real-time alert               | ✅ Implemented            |
| Event logging                 | ✅ Implemented            |
| CSV security log              | ✅ Implemented            |
| Monitoring dashboard          | 🔄 Prototype/Development |
| ANPR                          | 🔄 Future module         |
| Face recognition              | 🔄 Future module         |
| Suspicious activity detection | 🔄 Future module         |
| Night-time analytics          | 🔄 Future module         |
| Multi-camera deployment       | 🔄 Future module         |
| Command/control integration   | 🔄 Future module         |

> **Important:** The modules marked as future/development are not presented as completed features of the current prototype.

---

# 13. Planned Future Enhancements

## 13.1 Automatic Number Plate Recognition

ANPR can be integrated to identify vehicle number plates from CCTV footage.

Potential pipeline:

```text
Vehicle Detection
       ↓
Number Plate Detection
       ↓
Image Preprocessing
       ↓
OCR
       ↓
Vehicle Number
       ↓
Event Log
```

---

## 13.2 Face Recognition

A future module can detect and recognize faces where appropriate and legally authorized.

The system can potentially compare detected faces against an authorized database.

---

## 13.3 Suspicious Activity Detection

Future versions can analyze movement patterns and predefined rules to identify potentially suspicious activities.

Examples could include:

* Repeated movement near restricted areas
* Prolonged presence in sensitive zones
* Unusual movement patterns
* Multiple people entering restricted areas

Such events would require additional model development and validation.

---

## 13.4 Night-Time Detection

The system can be extended for low-light and night-time CCTV footage.

Potential techniques include:

* Low-light enhancement
* Infrared video support
* Image preprocessing
* Night-specific detection models

---

## 13.5 Multi-Camera Support

The platform can eventually support multiple CCTV cameras simultaneously.

Example:

```text
BOP-01 ─┐
BOP-02 ─┤
BOP-03 ─┼──► IBVAP Analytics Engine
BOP-04 ─┤
BOP-05 ─┘
```

Each camera can have its own:

* Camera ID
* Detection events
* Virtual fence
* Tracking information
* Alert history

---

## 13.6 Real-Time Alert System

Future versions can provide alerts through:

* Dashboard notifications
* Sound alerts
* Email
* SMS
* Command center notifications

---

## 13.7 Low-Bandwidth / Edge Deployment

Border locations may have limited network connectivity.

Future development will explore processing CCTV feeds locally or near the camera to reduce dependence on continuous high-bandwidth connectivity.

---

# 14. Advantages

IBVAP is designed around the following objectives:

### Software-Based Approach

The platform focuses on using existing CCTV infrastructure rather than requiring specialized surveillance hardware for every analytics capability.

### Automated Monitoring

AI-based detection can assist personnel by highlighting potentially important events.

### Real-Time Detection

The prototype processes video frames continuously and can generate an alert when a virtual-fence violation occurs.

### Event Logging

Security events are automatically recorded for later review.

### Scalable Architecture

The architecture can be extended from a single CCTV stream toward multiple cameras and additional AI modules.

### Cost-Conscious Design

Using software-based analytics with existing camera infrastructure can potentially reduce the need for dedicated hardware, subject to deployment requirements and performance validation.

---

# 15. Limitations of the Current Prototype

The current implementation is a prototype and has several limitations:

1. It currently uses recorded CCTV video rather than a complete live IP-camera deployment.
2. The virtual-fence configuration is currently predefined.
3. Detection performance depends on video quality, lighting, camera angle, and environmental conditions.
4. ANPR is not yet implemented.
5. Face recognition is not yet implemented.
6. Advanced suspicious-activity detection is not yet implemented.
7. Night-time optimization is not yet implemented.
8. The current event log uses CSV storage.
9. Large-scale multi-camera deployment requires additional optimization and testing.
10. Real-world border deployment would require extensive testing, security review, privacy safeguards, and operational validation.

---

# 16. Testing

The prototype is tested using CCTV video input.

### Test Case 1 – Person Detection

**Input:** CCTV footage containing a person.

**Expected Result:**
The person is detected with a bounding box.

**Result:** Successful.

---

### Test Case 2 – Vehicle Detection

**Input:** CCTV footage containing vehicles.

**Expected Result:**
Vehicles are detected and classified by the object detection model.

**Result:** Successful where supported by the model and video quality.

---

### Test Case 3 – Object Tracking

**Input:** Moving person/vehicle.

**Expected Result:**
The object receives a persistent tracking ID.

**Result:** Successful.

---

### Test Case 4 – Virtual Fence Intrusion

**Input:** Tracked person crossing the virtual boundary.

**Expected Result:**

```text
!!! INTRUSION DETECTED !!!
```

**Result:** Successful.

---

### Test Case 5 – Event Logging

**Input:** Intrusion event.

**Expected Result:**
The event is stored in `alerts.csv`.

**Result:** Successful.

---

# 17. Security Considerations

Since the proposed system is intended for security-sensitive environments, future deployment should consider:

* Secure camera communication
* Authentication and authorization
* Encrypted data transmission
* Secure event storage
* Access control
* Audit logging
* Protection of recorded video
* Privacy and data-protection requirements
* Secure model and software updates

The current prototype focuses primarily on the Computer Vision and event-detection pipeline.

---

# 18. Ethical and Privacy Considerations

The platform is intended as a decision-support and surveillance analytics system.

Any future implementation involving face recognition, vehicle identification, or individual tracking should operate according to applicable laws, policies, authorization requirements, retention rules, and privacy safeguards.

AI-generated alerts should be treated as detection signals requiring appropriate operational verification rather than automatically assuming that every detection represents a confirmed security incident.

---

# 19. Project Demonstration

The current prototype demonstration follows this sequence:

```text
1. Start the application
        ↓
2. Load CCTV footage
        ↓
3. Detect people and vehicles
        ↓
4. Assign tracking IDs
        ↓
5. Monitor virtual fence
        ↓
6. Detect fence crossing
        ↓
7. Generate intrusion alert
        ↓
8. Store event in alerts.csv
        ↓
9. Display event through dashboard
```

### Demonstration Command

```bash
python main.py
```

---

# 20. Prototype Demonstration Video

A short screen recording of the working prototype can be included here.

**Prototype Demo:**
[Watch IBVAP Prototype Demo](YOUR_UNLISTED_YOUTUBE_LINK)

> The demonstration video shows the current working prototype and should not be interpreted as evidence that future modules such as ANPR, face recognition, or advanced behavior analytics are already implemented.

---

# 21. Expected Impact

The long-term objective of IBVAP is to provide an AI-assisted surveillance platform capable of analyzing existing CCTV infrastructure and helping security personnel identify potentially important events more efficiently.

The platform is intended to support:

* Faster identification of intrusion events
* Automated video analytics
* Reduced dependence on continuous manual observation
* Centralized event monitoring
* Historical event analysis
* Extensible AI-based surveillance capabilities

---

# 22. Conclusion

IBVAP demonstrates the feasibility of applying AI and Computer Vision to CCTV-based border surveillance.

The current prototype successfully establishes the core pipeline:

```text
CCTV
 ↓
YOLO Detection
 ↓
Object Tracking
 ↓
Virtual Fence
 ↓
Intrusion Detection
 ↓
Alert
 ↓
Event Logging
```

This provides the foundation for the next development stages, including ANPR, face recognition, advanced activity analysis, night-time analytics, multi-camera support, and integration with centralized command and control systems.

The project is currently presented as a **40% prototype implementation**, with future modules clearly separated from the features already demonstrated.

---

# 23. Team / Project Information

**Project:** IBVAP – Intelligent Border Video Analytics Platform

**Organization:** Ministry of Home Affairs

**Department:** Sashastra Seema Bal (SSB), Police II Division

**Category:** Software

**Theme:** Blockchain & Cybersecurity

**Domain:** Artificial Intelligence / Computer Vision / Video Analytics

**Current Stage:** Prototype – approximately 40% implementation

---

## Keywords

`Artificial Intelligence`
`Computer Vision`
`YOLO`
`YOLO11`
`Object Detection`
`Object Tracking`
`ByteTrack`
`CCTV Analytics`
`Border Surveillance`
`Intrusion Detection`
`Virtual Fence`
`Real-Time Alerts`
`Video Analytics`
`Python`
`OpenCV`
`Streamlit`
`Security Analytics`
