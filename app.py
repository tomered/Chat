from flask import Flask, request, jsonify, render_template
from datetime import datetime, timezone
import csv
import os


# os.system('clear')

# Immplemented by Erik
CHAT_LOG_FIELDS = ['room', 'date', 'time', 'username', 'message']
FILE_PATH = './chat_log/chat.csv'
if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
    with open(FILE_PATH, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(CHAT_LOG_FIELDS)


app = Flask(__name__)


# Implemented by Tomer
@app.route("/<room>", methods= ['GET'])
def room(room):
    return render_template("index.html")


# Implemented by Erik
@app.route('/api/chat/<room>', methods=['GET', 'POST'])
def chat(room):
    if request.method == 'POST':
        username = request.form.get('username')
        message = request.form.get('msg')

        if not username or not message:
            print(username, message)
            return jsonify({"error": "Username and message are required"}), 400

        now = datetime.now(timezone.utc)
        chat_entry = {
            "room": room,
            "date": now.strftime('%Y-%m-%d'),
            "time": now.strftime('%H:%M:%S'),
            "username": username,
            "message": message
        }

        with open(FILE_PATH, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(chat_entry.values())

        return jsonify({"chat": chat_entry, "success": True}), 201


if __name__ == "__main__":
    app.run()
