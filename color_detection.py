import cv2
import numpy as np

class ColorDetector:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def get_color_name(self, r, g, b):

        if r > 200 and g > 200 and b > 200:
            return "White"

        elif r < 60 and g < 60 and b < 60:
            return "Black"

        elif r > 180 and g < 100 and b < 100:
            return "Red"

        elif g > 180 and r < 100 and b < 100:
            return "Green"

        elif b > 180 and r < 100 and g < 100:
            return "Blue"

        elif r > 180 and g > 180 and b < 100:
            return "Yellow"

        elif r > 180 and g > 100 and b < 100:
            return "Orange"

        elif r > 150 and b > 150 and g < 120:
            return "Purple"

        elif r > 180 and g > 150 and b > 150:
            return "Pink"

        else:
            return "Unknown"

    def generate_frames(self):

        while True:

            success, frame = self.cap.read()

            if not success:
                break

            h, w, _ = frame.shape

            cx = w // 2
            cy = h // 2

            b, g, r = frame[cy, cx]

            color_name = self.get_color_name(r, g, b)

            cv2.circle(frame, (cx, cy), 6, (255, 255, 255), -1)

            text = f"{color_name} RGB({r},{g},{b})"

            cv2.putText(
                frame,
                text,
                (10, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

            _, buffer = cv2.imencode(".jpg", frame)

            frame = buffer.tobytes()

            yield (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' +
                frame +
                b'\r\n'
            )