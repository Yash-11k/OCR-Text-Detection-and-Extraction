from flask import Flask, render_template, request
import os
from ocr import extract_text

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():

    extracted_text = ""

    if request.method == "POST":

        file = request.files["image"]

        if file:

            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

            file.save(filepath)

            extracted_text = extract_text(filepath)

    return render_template("index.html", text=extracted_text)


if __name__ == "__main__":
    app.run(debug=True)