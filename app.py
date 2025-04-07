from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

def time_difference_in_seconds(t1: str, t2: str) -> int:
    # Define the time format
    time_format = "%a %d %b %Y %H:%M:%S %z"
    
    # Parse the timestamps
    time1 = datetime.strptime(t1, time_format)
    time2 = datetime.strptime(t2, time_format)
    
    # Return the absolute difference in seconds
    return abs(int((time1 - time2).total_seconds()))

@app.route('/time_diff', methods=['POST'])
def calculate_time_difference():
    data = request.json
    results = []
    
    # Process each pair of timestamps
    for t1, t2 in data.get('timestamps', []):
        results.append(time_difference_in_seconds(t1, t2))
    
    # Get the node id from the environment variable
    node_id = request.environ.get('NODE_ID', 'unknown')
    
    # Return the results with the node ID
    return jsonify({
        "id": node_id,
        "result": results
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
