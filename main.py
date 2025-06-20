from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

@app.route("/api/audio/upload", methods=["POST"])
def upload_audio():
    file = request.files.get("file")
    if not file:
        return jsonify({"message": "No audio file provided"}), 400
    return jsonify({"message": "File received", "filename": file.filename}), 200

app.run(host="0.0.0.0", port=10000)
