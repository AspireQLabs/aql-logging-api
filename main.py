from flask import Flask, request, jsonify, render_template
import json
import datetime
import os

app = Flask(__name__)

LOG_FILE = 'log_data.jsonl'

# Endpoint to receive log data
@app.route('/log', methods=['POST'])
def log_data():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No JSON payload'}), 400

        data['timestamp'] = datetime.datetime.utcnow().isoformat()

        with open(LOG_FILE, 'a') as f:
            f.write(json.dumps(data) + '\n')

        return jsonify({'message': 'Log received'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to return all logs
@app.route('/logs', methods=['GET'])
def get_logs():
    try:
        logs = []
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r') as f:
                for line in f:
                    logs.append(json.loads(line.strip()))
        return jsonify(logs), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Web interface
@app.route('/')
def index():
    return render_template('index.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
