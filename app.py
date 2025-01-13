from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ACCESS_TOKEN = 'APP_USR-1327720301595288-010709-255c6b5553819ffd402c86aa264f8dca-186633568'

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.content_type != 'application/json':
        return jsonify({'error': 'Content-Type must be application/json'}), 415

    data = request.json
    print(f"Notificação de pagamento recebida: {data}")
    
    payment_id = data['data']['id']  # ID do pagamento recebido
    status = data['data']['status']  # Status do pagamento (aprovado, pendente, etc.)

    if status == 'approved':
        print(f"Pagamento aprovado! ID: {payment_id}")
        # Aqui você pode realizar outras ações, como atualizar o status no banco de dados
    else:
        print(f"Pagamento não aprovado. Status: {status}")
    
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
