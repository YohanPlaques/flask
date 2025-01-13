const express = require('express');
const axios = require('axios');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

app.post('/notificacao', async (req, res) => {
  try {
    const data = req.body;
    console.log('Dados recebidos:', data);

    if (!data || !data.status || !data.maquina || !data.amount) {
      console.log('Notificação sem dados suficientes:', data);
      return res.status(400).send('Dados inválidos');
    }

    if (data.status === 'approved') {
      console.log(`Pagamento aprovado para a ${data.maquina}`);

      const valorPagamento = data.amount;
      const valorEsperado = 100;  // Valor esperado para acionar a lâmpada

      if (valorPagamento === valorEsperado) {
        console.log(`Pagamento de ${valorPagamento} recebido. Acionando a lâmpada da ${data.maquina}...`);

        try {
          const esp32Url = `http://IP_DO_ESP32_${data.maquina}/acionar-lampada`;  // Envia comando para o ESP32
          const response = await axios.get(esp32Url);
          console.log('Comando enviado ao ESP32:', response.data);
        } catch (error) {
          console.error('Erro ao enviar comando para o ESP32:', error);
        }
      } else {
        console.log(`Pagamento de ${valorPagamento} não corresponde ao valor esperado.`);
      }
    }

    res.status(200).send('Recebido');
  } catch (error) {
    console.error('Erro ao processar a notificação:', error);
    res.status(500).send('Erro no servidor');
  }
});

app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`);
});
