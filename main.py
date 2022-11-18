from flask import Flask, request

app = Flask(__name__)

global_dict = {
        "servo1": 0,
        "servo2": 0,
        "servo3": 0,
        "servo4": 0,
        "servo5": 0
    }

@app.route("/")
def root():
    global global_dict
    return global_dict

@app.route("/send_data", methods=["GET", "POST"])
def send_data():
    global global_dict
    global_dict = request.json
    return {"message": "success"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
