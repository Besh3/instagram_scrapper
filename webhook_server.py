from flask import Flask, request, jsonify
from typing import Union, Tuple
import requests

app = Flask(__name__)

callback_url = 'https://chimp-fun-cicada.ngrok-free.app/'  # Ngrok URL
verify_token = '12345'  # Generated own token
instagram_account_id = '17841406879294936'
page_id = '100844919771658'
app_id = '847655893544016'
access_token = 'EAAMC8ERtLFABOZC2zJZBq5ZBsrpjR2qhIfV3BQ7zMKTVMH0yNnBg1kUMVsLLEfO2bGGhhIyVssnmWdcMwb2szsCvdNgu5T5mgB3gZBEKwCNwBXV7vmoMxair3LZAZBTAmiYp49ReCEf0IO5uZA1UtWcFk5dPYJc1XjpnyNU04shGly8KL4qRaKgLB9sAxaVyxf6aq9U17Sx'  # Replace with your Instagram access token

# Register Instagram webhook
def register_instagram_webhook():
    params = {
        'object': 'user',
        'fields': 'mention_media,mentioned_comments',
        'callback_url': callback_url,
        'verify_token': verify_token,
        'access_token': access_token,
    }

    response = requests.post(f'https://graph.facebook.com/v17.0/{app_id}/subscriptions', params=params)
    
    if response.status_code == 200:
        return 'Webhook registered successfully.'
    else:
        return 'Webhook registration failed.'

@app.route('/webhooks', methods=['POST'])
def webhook():
    data = request.json
    print("Received webhook data:")
    print(data)
    # Handle the webhook data here (e.g., process Instagram mentions)

    # Check the object type in the data to determine if it's a mention or mentioned comment
    object_type = data.get('object') if data is not None else None

    if object_type == 'mentioned_media':
        # Handle mention event
        print('Received a mention event:')
        print(data)
    elif object_type == 'mentioned_comment':
        # Handle mentioned comment event
        print('Received a mentioned comment event:')
        print(data)

    return jsonify({'status': 'ok'})

@app.route('/register-webhook', methods=['GET'])
def register_webhook_route() -> Union[Tuple[str, int], Tuple[str, int]]:
    # Extract query parameters from the request
    hub_mode = request.args.get('hub.mode')
    hub_challenge = request.args.get('hub.challenge')
    hub_verify_token = request.args.get('hub.verify_token')

    # Debugging: Print request data
    print(f'hub_mode: {hub_mode}')
    print(f'hub_challenge: {hub_challenge}')
    print(f'hub_verify_token: {hub_verify_token}')

    # Check if the provided verify token matches your token
    if hub_verify_token == verify_token and hub_mode == 'subscribe':
        print('Verification succeeded')
        hub_challenge_str = str(hub_challenge)
        return hub_challenge_str, 200
    else:
        print('Verification failed')
        return 'Verification failed', 403

if __name__ == '__main__':
    # Register Instagram webhook when the application starts
    register_instagram_webhook()
    #register_webhook_route()
    app.run(host='0.0.0.0', port=5000, debug=True)
