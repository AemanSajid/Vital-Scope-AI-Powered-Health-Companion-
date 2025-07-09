from flask import Flask, request, jsonify
from flask_cors import CORS
from fuzzywuzzy import process
import json

app = Flask(__name__)
CORS(app)  # Enable CORS so Streamlit can access this

# Load FAQ data
with open("faq_data.json", "r") as f:
    faq = json.load(f)

def find_best_match(user_input):
    match, score = process.extractOne(user_input, faq.keys())
    if score >= 70:
        return match
    return None

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_question = data.get("question", "").lower().strip()
    match = find_best_match(user_question)

    if match:
        entry = faq[match]
        return jsonify({
            "answer": entry["answer"],
            "related": entry.get("related", [])
        })
    else:
        return jsonify({
            "answer": "❌ I'm sorry, I don't have a direct answer to that specific question. For further queries, please email us at: ammasajid@gmail.com",
            "related": []
        })

if __name__ == "__main__":
    app.run(debug=True)
