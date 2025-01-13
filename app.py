from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ACCESS_TOKEN = 'APP_USR-1327720301595288-010709-255c6b5553819ffd402c86aa264f8dca-186633568'

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.content_type != 'application/json':
        return jsonify({'error': 'Content-Type must be application/json'}), 415

    data = request.json
    payment_id = data['data']['id']  # Pegue o ID do pagamento da notificação
    
    # Consultar a API do Mercado Pago para verificar o status do pagamento
    url = f'https://api.mercadopago.com/v1/payments/{payment_id}'
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
    
    response = requests.get(url, headers=headers)
    payment_data = response.json()

    if payment_data['status'] == 'approved':
        # Lógica para processar pagamento aprovado
        machine_id = data['data']['additional_info']['items'][0]['id']  # ID do caixa
        amount = data['data']['amount']  # Valor do pagamento
        
        print(f"Pagamento aprovado! Máquina ID: {machine_id}, Valor: {amount}")
    else:
        # Lógica para processar pagamentos não aprovados
        print(f"Pagamento não aprovado. Status: {payment_data['status']}")

    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
