from flask import request, jsonify, render_template
from app import app
from app.GPIOSwitcher import GPIOSwitcher

GPIOSwitcher.setup()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route("/start", methods=["POST"])
def start():
    data = request.get_json()
    ref = data.get('ref')
    delay = float(data.get('delay'))
    GPIOSwitcher.start(delay, ref)
    data = get_status()
    return data
 


@app.route("/stop", methods=["POST"])
def stop():
    data = request.get_json()
    ref = data.get('ref')
    GPIOSwitcher.stop(ref)
    data = get_status()
    return data


@app.route("/status", methods=["GET"])
def get_status():
    ref1, ref2, ref1_time, ref2_time = GPIOSwitcher.get_status()
    return jsonify({"ref1": ref1, "ref2": ref2, "ref1_time":ref1_time, "ref2_time":ref2_time,}), 200
