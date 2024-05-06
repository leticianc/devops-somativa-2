import requests

def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    response = requests.post(url, params=params)
    if response.status_code == 200:
        print("Mensagem enviada com sucesso para o Telegram!")
    else:
        print("Erro ao enviar mensagem para o Telegram.")

if __name__ == "__main__":
    # Substitua 'SEU_TOKEN_DO_BOT' pelo token do seu bot e 'SEU_CHAT_ID' pelo ID do seu chat
    bot_token = '7184171343:AAGPI6Dr_ISC2l9qGmAmgOhY_RdmMDDxoZ4'
    chat_id = '6808919876'
    message = 'Olá! Uma nova solicitação de pull foi aberta no repositório.'
    send_telegram_message(bot_token, chat_id, message)
