from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        "name": request.form.get('name'),
        "email": request.form.get('email'),
        "message": request.form.get('message'),
        "timestamp": datetime.utcnow().isoformat()
    }

    with open("messages.json", "a") as f:
        f.write(json.dumps(data) + "\n")

    return jsonify({"status": "success", "data": data})

if __name__ == '__main__':
    app.run(debug=True)
