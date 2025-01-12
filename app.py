from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Dados enviados pelo Mercado Pago
    print(data)  # Apenas para testar e ver o conteúdo

    # Aqui você pode adicionar a lógica para processar a notificação, por exemplo:
    # Verificar se o pagamento foi aprovado, etc.

    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
