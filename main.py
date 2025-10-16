from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/fishit', methods=['POST'])
def receive_fish_data():
    try:
        data = request.get_json()

        player = data.get("player")
        fish = data.get("fish")
        weight = data.get("weight")
        coins = data.get("coins")

        log = f"[{datetime.datetime.now()}] {player} menangkap {fish} ({weight}kg) → +{coins} coins"
        print(log)

        with open("fishit_log.txt", "a", encoding="utf-8") as f:
            f.write(log + "\n")

        return jsonify({"status": "success", "message": "Data diterima"}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/')
def index():
    return "✅ FishIt Webhook Aktif", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
