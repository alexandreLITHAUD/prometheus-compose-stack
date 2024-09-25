from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        alert_data = request.json
        logging.info(f"Received alert: {alert_data}")
        # You can process the alert data here as needed
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid request method"}), 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)