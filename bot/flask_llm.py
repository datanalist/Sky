from flask import Flask, request, jsonify

app = Flask(__name__)

system = "You are a helpful AI code assistant"

@app.route("/generate_text", methods=["POST"])
def generate_text():
    data = request.json
    
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