import cv2
import mediapipe as mp
import serial
import math
import time

webcam = cv2.VideoCapture(0)
mp_face = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

try:
    arduino = serial.Serial("COM5", 9600)
    time.sleep(2)
except Exception as e:
    print("Arduino serial connection failed:", e)
    arduino = None

with mp_face.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
    while True:
        ret, frame = webcam.read()
        if not ret:
            break
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb)
        height, width, channels = frame.shape

        if result.multi_face_landmarks:
            print("Face detected!", flush=True)
            for face_landmarks in result.multi_face_landmarks:
                if len(face_landmarks.landmark) > max(306, 61):
                    pt1 = face_landmarks.landmark[306]
                    pt2 = face_landmarks.landmark[61]
                    x1, y1 = int(pt1.x * width), int(pt1.y * height)
                    x2, y2 = int(pt2.x * width), int(pt2.y * height)

                    cv2.circle(frame, (x1, y1), 3, (0, 0, 255), 5)
                    cv2.circle(frame, (x2, y2), 3, (0, 0, 255), 5)
                    cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

                    distance = math.hypot(x2 - x1, y2 - y1)
                    print("Distance:", distance, flush=True)


                    if distance>55:
                        arduino.write(b"A")
                    elif distance<55:
                        arduino.write(b"B")

        cv2.imshow("final", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

webcam.release()
cv2.destroyAllWindows()
if arduino:
    arduino.close()

