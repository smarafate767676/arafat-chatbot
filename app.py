from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("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")  # Secret key

@app.route("/")
def home():
    return "Arafat's Chatbot is Running!"

@app.route("/ask", methods=["POST"])
def ask():
    user_msg = request.json["message"]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a helpful chatbot."},
            {"role": "user", "content": user_msg}
        ]
    )
    return jsonify({"reply": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    app.run()
