from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO

app = Flask(__name__)

camera = cv2.VideoCapture(0)
model = YOLO("yolov8n.pt")

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break

        results = model(frame)
        garbage_detected = False

        for result in results:
            for box in result.boxes:
                cls = int(box.cls[0])
                label = model.names[cls]

                if label in ["bottle", "cup", "banana", "apple", "plastic"]:
                    garbage_detected = True
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, "Garbage Detected",
                                (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.8,
                                (0, 255, 0),
                                2)

        if not garbage_detected:
            cv2.putText(frame, "No Garbage",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 0, 255),
                        2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
