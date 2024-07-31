from flask import request, jsonify, render_template
from app import app
import gpio


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/push-button", methods=["POST"])
def push_button():
    data = request.get_json()
    action = data.get('action')

    if action == 'on':
        # GPIO.output(RELAY_PIN, GPIO.HIGH)
        print("Ballin")
        return jsonify({"status": "Relay turned on"}), 200
    elif action == 'off':
        # GPIO.output(RELAY_PIN, GPIO.LOW)
        print("Jover")
        return jsonify({"status": "Relay turned off"}), 200
    else:
        return jsonify({"error": "Invalid action"}), 400
