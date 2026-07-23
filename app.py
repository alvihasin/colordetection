from flask import Flask, render_template, Response
from color_detection import ColorDetector

app = Flask(__name__)

detector = ColorDetector()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video")
def video():

    return Response(
        detector.generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    app.run(debug=True)