from flask import Flask, request, jsonify
import requests
import time
from flask_cors import CORS

app = Flask(_name_)
CORS(app)  # Enable CORS so frontend (HTML/JS) can access this server

@app.route('/check', methods=['POST'])
def check_url():
    data = request.get_json()
    url = data.get('url')
    
    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        end_time = time.time()
        response_time = round(end_time - start_time, 2)

        return jsonify({
            'response_time': response_time,
            'status_code': response.status_code
        })

    except Exception as e:
        return jsonify({
            'error': str(e),
            'response_time': None,
            'status_code': None
        }), 500

if _name_ == '_main_':
    app.run(debug=True)