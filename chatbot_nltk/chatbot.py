import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk
from nltk.tokenize import word_tokenize
import re

nltk.download("punkt")

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()

    user_message = re.sub(r"[^\w\s]", "", user_message)

    tokens = word_tokenize(user_message)

    if any(w in tokens for w in ["hi", "hello", "hey"]):
        reply = "Hi 👋 I can help you with registration, login, appointments, or medical queries."

    elif any(w in tokens for w in ["register", "signup", "sign"]):
        reply = "To register, enter your email, password, confirm password, and click Register."

    elif "login" in tokens:
        reply = "Use your registered email and password to login."

    elif any(w in tokens for w in ["book", "booking"]):
        reply = "To book an appointment, login first, then choose a doctor and time slot."

    elif "appointment" in tokens:
        reply = "Appointments can be booked after login from the appointment page."

    elif any(w in tokens for w in ["doctor", "doctors"]):
        reply = "Doctors are available after login. Select a department to view doctors."

    elif "password" in tokens:
        reply = "If you forgot your password, please register again or contact admin support."

    elif any(w in tokens for w in ["contact", "help", "support"]):
        reply = "You can contact the hospital helpdesk during working hours."

    elif any(w in tokens for w in ["time", "timing", "hours"]):
        reply = "Hospital working hours are 9 AM to 5 PM, Monday to Saturday."

    elif any(w in tokens for w in ["fever", "cold", "cough"]):
        reply = "For fever, cold, or cough, please consult a General Physician."

    elif any(w in tokens for w in ["headache", "migraine"]):
        reply = "Headache or migraine issues may require consultation with a Neurologist."

    elif any(w in tokens for w in ["bp", "pressure", "hypertension"]):
        reply = "High blood pressure patients should consult a Cardiologist."

    elif any(w in tokens for w in ["diabetes", "sugar"]):
        reply = "Diabetes patients should consult an Endocrinologist."

    elif any(w in tokens for w in ["skin", "rash", "allergy"]):
        reply = "Skin problems can be treated by a Dermatologist."

    elif any(w in tokens for w in ["eye", "vision"]):
        reply = "Eye-related problems should be consulted with an Ophthalmologist."

    elif any(w in tokens for w in ["child", "baby", "kids"]):
        reply = "For child health issues, please consult a Pediatrician."

    elif "emergency" in tokens:
        reply = "🚨 This is an emergency. Please visit the nearest hospital immediately."

    else:
        reply = (
            "I can help with:\n"
            "• Registration & Login\n"
            "• Booking Appointments\n"
            "• Doctor information\n"
            "• Basic medical guidance\n"
            "• Emergency help•"
        )

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)

