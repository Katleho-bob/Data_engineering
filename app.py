from flask import Flask, request, jsonify
from datetime import datetime
import pytz
import os

app = Flask(__name__)

# Fetch NODE_ID from the environment variable
NODE_ID = os.getenv('NODE_ID', 'unknown')

def parse_timestamp(ts):
    return datetime.strptime(ts, '%a %d %b %Y %H:%M:%S %z')

@app.route('/timestamp-diff', methods=['POST'])
def timestamp_diff():
    data = request.data.decode('utf-8').strip().split('\n')
    T = int(data[0])
    results = []

    for i in range(T):
        t1 = parse_timestamp(data[2 * i + 1])
        t2 = parse_timestamp(data[2 * i + 2])
        diff = abs(int((t1 - t2).total_seconds()))
        results.append(str(diff))

    # Return the response with the NODE_ID and results
    response = {
        "id": NODE_ID,
        "result": results
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
