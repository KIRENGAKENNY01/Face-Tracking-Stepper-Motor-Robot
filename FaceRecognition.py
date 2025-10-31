import cv2
import numpy as np
import time
import serial

# =============================
# SERIAL COMMUNICATION SETUP
# =============================
# Change 'COM3' to your Arduino port (Windows) or '/dev/ttyUSB0' on Linux/Mac
arduino = serial.Serial('COM15', 9600, timeout=1)
time.sleep(2)  # wait for Arduino to initialize

# =============================
# CONFIGURATION
# =============================
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
CENTER_THRESHOLD = 80

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

print("🎥 Face Tracking with Arduino Control Started!")
print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(80, 80))

    frame_center_x = FRAME_WIDTH // 2
    movement_direction = "CENTERED"

    if len(faces) > 0:
        x, y, w, h = max(faces, key=lambda f: f[2] * f[3])
        face_center_x = x + w // 2
        offset_x = face_center_x - frame_center_x

        if offset_x < -CENTER_THRESHOLD:
            movement_direction = "LEFT"
        elif offset_x > CENTER_THRESHOLD:
            movement_direction = "RIGHT"
        else:
            movement_direction = "CENTERED"

        # Draw tracking visuals
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.circle(frame, (face_center_x, y + h // 2), 5, (0, 0, 255), -1)
    else:
        movement_direction = "CENTERED"

    # Send command to Arduino
    arduino.write((movement_direction + "\n").encode())

    # Display info
    cv2.putText(frame, f"Direction: {movement_direction}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow("Auto Face Tracker", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
arduino.close()
cv2.destroyAllWindows()
print("👋 Tracking stopped.")
