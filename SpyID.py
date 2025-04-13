from telethon.sync import TelegramClient
from telethon.errors import UsernameNotOccupiedError
from datetime import datetime

# Substitua com seu api_id e api_hash
api_id = 
api_hash = ''

# Função para registrar no log
def registrar_log(mensagem):
    with open("logs.txt", "a", encoding="utf-8") as log_file:
        log_file.write(mensagem + "\n")
        log_file.flush()  # força gravação imediata no disco

with TelegramClient('session_name', api_id, api_hash) as client:
    while True:
        username = input("\nEnter the person's @username: ").strip()

        if username.startswith('@'):
            username = username[1:]

        try:
            user = client.get_entity(username)
            resultado = (
                f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"
                f"\nUsername: @{user.username}"
                f"\nNome: {user.first_name}"
                f"\nID: {user.id}"
                f"\n------------------------------"
            )
            print(resultado)
            registrar_log(resultado)

        except UsernameNotOccupiedError:
            erro = (
                f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"
                f"\n❌ Username não encontrado: @{username}"
                f"\n------------------------------"
            )
            print(erro)
            registrar_log(erro)

        except Exception as e:
            erro = (
                f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"
                f"\n⚠️ Erro ao buscar @{username}: {e}"
                f"\n------------------------------"
            )
            print(erro)
            registrar_log(erro)
