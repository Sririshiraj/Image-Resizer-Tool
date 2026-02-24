from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# ----------------------------
# Rule-Based Chatbot Function
# ----------------------------
def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi"]:
        return "Hello there! How can I help you today?"

    elif user_input == "how are you":
        return "I'm just a program, but I'm doing great! How about you?"

    elif user_input == "your name":
        return "I am a simple rule-based chatbot running on a server."

    elif user_input == "what can you do":
        return "I can answer simple questions based on predefined rules."

    elif user_input == "bye":
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that. Can you try something else?"


# ----------------------------
# Routes
# ----------------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    response = chatbot_response(user_message)
    return jsonify({"response": response})


# ----------------------------
# Run Server
# ----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)