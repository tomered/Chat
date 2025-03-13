from flask import request, jsonify, render_template
from models import Chat
from datetime import datetime, timezone
import csv
import os


# Immplemented by Erik
NOW = datetime.now(timezone.utc)
CHAT_LOG_FIELDS = ['room', 'date', 'time', 'username', 'message']
FILE_PATH = './chat.csv'
if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
    with open(FILE_PATH, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(CHAT_LOG_FIELDS)


def register_routes(app, db):

    # Implemented by Tomer
    @app.route("/")
    def home():
        return render_template("index.html")

    # Implemented by Tomer

    @app.route("/<room>", methods=['GET'])
    def room(room):
        return render_template("index.html")

    # Implemented by Erik

    @app.route('/api/chat/<room>', methods=['GET', 'POST'])
    def chat(room):
        username = request.form.get('username')
        message = request.form.get('msg')

        if request.method == 'POST':
            if not username or not message:
                print(username, message)
                return jsonify({"error": "Username and message are required"}), 400

            chat_entry = Chat(
                room=room,
                date=NOW.strftime('%Y-%m-%d'),
                time=NOW.strftime('%H:%M:%S'),
                username=username,
                message=message,
            )

            db.session.add(chat_entry)
            db.session.commit()

            return jsonify(chat_entry.to_dict(), 201)

        # Implemented by Sharon
        elif request.method == 'GET':
            chat_entries = db.session.execute(
                db.select(Chat).filter_by(room=room)).scalars().all()
            chat_data = "\n".join(
                f"[{entry.date} {entry.time}] {entry.username}: {entry.message}"
                for entry in chat_entries
            )

            return chat_data
