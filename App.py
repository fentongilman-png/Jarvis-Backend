from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.environ.get("OPENAI_API_KEY")

@app.route("/jarvis", methods=["POST"])
def jarvis():
    user_input = request.json.get("message", "")

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "You are JARVIS, a fast, intelligent AI assistant. Be clear and direct."},
                {"role": "user", "content": user_input}
            ]
        }
    )

    data = response.json()

    try:
        reply = data["choices"][0]["message"]["content"]
    except:
        reply = "Error processing request."

    return jsonify({"reply": reply})

@app.route("/")
def home():
    return "JARVIS backend is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
