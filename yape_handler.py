from flask import Flask, request, jsonify
import json
app = Flask(__name__)

last_report = []

@app.route('/handler/payments', methods=['POST', 'GET'])
def managePayments():
    global last_report
    if request.method == 'POST':
        last_report.append(json.loads(request.data))
        # last_report = request.form
        return jsonify(success=200)
    return jsonify(last_report)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
