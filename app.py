from flask import Flask, render_template, request, jsonify

from utils.chatbot import chatbot

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get("message", "").strip()

    if not user_message:

        return jsonify({
            "reply": "Please enter a question.",
            "matched_question": None,
            "similarity": 0
        })

    response = chatbot.get_response(user_message)

    return jsonify(response)


import os

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 8000))

    app.run(

        host="0.0.0.0",

        port=port

    )