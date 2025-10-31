# **Face-Tracking Stepper Motor Robot**  
### *Intelligent Robotics Project – Phase 1 & 2*  


---

## Overview
This project implements a **real-time face-tracking system** using **OpenCV** in Python. When a face is detected and moves:
- The **direction** (`LEFT`, `RIGHT`, `UP`, `DOWN`) is calculated.
- A **stepper motor** (via Arduino) **rotates** to follow the face.

**Phase 1:** Face detection + visual feedback  
**Phase 2:** Serial communication + stepper motor control

---

## Features
| Feature | Status |
|-------|--------|
| Live face detection (Haar Cascade) | Done |
| Real-time direction & speed tracking | Done |
| 640x480 optimized video feed | Done |
| FPS counter | Done |
| Serial communication with Arduino | Done |
| Stepper motor follows face | Done |

---

## Hardware Required
- **Webcam** (Logitech USB recommended)
- **Arduino Uno / Nano**
- **Stepper Motor** + **A4988 / DRV8825 Driver**
- **Jumper wires**
- **12V Power supply** (for stepper)

---

## Software Requirements
| Tool | Version |
|------|--------|
| Python | 3.9+ |
| OpenCV | `4.12.0` |
| PySerial | `3.5` |
| Arduino IDE | Latest |

---

## Project Structure
```
FaceRecognition/
│
├── FaceRecognition.py          ← Main Python script (face tracking + serial)
├── arduino_stepper.ino         ← Arduino code (receives direction, moves motor)
├── haarcascade_frontalface_default.xml ← (auto-loaded by OpenCV)
├── venv/                       ← Virtual environment
└── README.md                   ← This file
```

---

## Setup Instructions

### 1. **Clone / Create Project Folder**
```bash
mkdir FaceRecognition && cd FaceRecognition
```

### 2. **Create Virtual Environment**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. **Install Python Dependencies**
```bash
pip install opencv-python numpy pyserial
```

### 4. **Arduino Setup**
1. Open `arduino_stepper.ino` in Arduino IDE
2. Connect Arduino via USB
3. Upload the sketch
4. Note the **COM port** (e.g., `COM3`)

---

## Wiring (Arduino + Stepper)

| Arduino | A4988 Driver |
|--------|--------------|
| `8`    | `DIR` (Direction) |
| `9`    | `STEP` (Pulse) |
| `GND`  | `GND` |
| `5V`   | `VCC` (logic) |

> Connect stepper coils to `A1,A2,B1,B2` on driver  
> Power driver with **12V external supply**

---

## Run the System

### Step 1: Start Arduino
- Ensure `arduino_stepper.ino` is uploaded
- Arduino listens on **9600 baud**

### Step 2: Run Python Script
```powershell
python FaceRecognition.py
```

> **Update COM port** in Python script if needed:
```python
ser = serial.Serial('COM3', 9600, timeout=1)  # ← Change COM3
```

---

## How It Works

1. **Camera captures frame**
2. **Face detected → center calculated**
3. **Offset from screen center** → direction
4. **Direction sent via serial** (`L`, `R`, `C`)
5. **Arduino receives command**
6. **Stepper rotates** accordingly

---

## Serial Protocol (Python → Arduino)

| Command | Meaning |
|--------|--------|
| `L`    | Move **Left** |
| `R`    | Move **Right** |
| `C`    | **Center** (stop) |

---

## Calibration Tips

- Adjust `CENTER_THRESHOLD` in Python for sensitivity
- Tune `STEPS_PER_REV` and `DELAY` in Arduino
- Face should be **1–3 feet** from camera
- Use **good lighting**

---

## Troubleshooting

| Issue | Solution |
|------|----------|
| `NO FACE` in daylight | Face camera, remove glasses/hat |
| Motor not moving | Check COM port, wiring, power |
| `Serial port not found` | Run `Get-COMPort` in PowerShell |
| Laggy video | Reduce resolution to `640x480` |
| Permission error | Run PowerShell as **Admin** |

---




**Made with love in Intelligent Robotics Lab**  
*Kenny – 2025*

---
