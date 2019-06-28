from flask import Flask, request
import json
app = Flask(__name__)

global last_report

@app.route('/handler/payments', methods=['POST', 'GET'])
def managePayments():
    global last_report
    if request.method == 'POST':
        last_report = json.loads(request.data)
        # last_report = request.form
        return json.dumps({"success": 200})
    return json.dumps(last_report, indent=4)

if __name__ == '__main__':
    app.run()
