from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/generate_text", methods=["POST"])
def generate_text():
    data = request.json
    system = "You are a helpful AI code assistant"
    conversation = [
        {
            "role" : "system",
            "content" : system
        },
        {
            "role" : "user",
            "content" : prompt

        }
    ]


    return jsonify({"text":generate_text})