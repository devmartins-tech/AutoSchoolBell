import os
import sys
import json
import schedule
import time
import pygame
from datetime import datetime

# Inicializa o módulo responsável pela reprodução de áudio.
pygame.mixer.init()

# Define o diretório base da aplicação.
# Quando executado como um executável (.exe), utiliza o diretório do próprio executável.
# Durante o desenvolvimento, utiliza o diretório onde o script está localizado.
if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Caminho do arquivo de configuração da aplicação.
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

# Caminho do arquivo de registro das execuções.
LOG_PATH = os.path.join(BASE_DIR, "logs", "logs.txt")

# Carrega as configurações da aplicação.
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)


def log(dia):
    """
    Registra a execução da sirene no arquivo de log.

    Args:
        dia (str): Nome do dia da semana em que a execução ocorreu.
    """
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

    with open(LOG_PATH, "a", encoding="utf-8") as log:
        log.write(
            f"[{datetime.now().replace(microsecond=0)}] | {dia} | Sirene executada com sucesso.\n"
        )


def tocar_semanal():
    """
    Identifica o dia da semana, seleciona o áudio correspondente
    e inicia sua reprodução.

    Aos finais de semana nenhuma ação é executada.
    """

    dia = datetime.now().weekday()

    if dia == 0:
        arquivo = os.path.join(BASE_DIR, "audio", config["audios"]["segunda"])
        print(f"[{datetime.now().replace(microsecond=0)}] | Segunda | Sirene executada com sucesso.")
        log("Segunda")

    elif dia == 1:
        arquivo = os.path.join(BASE_DIR, "audio", config["audios"]["terca"])
        print(f"[{datetime.now().replace(microsecond=0)}] | Terça | Sirene executada com sucesso.")
        log("Terça")

    elif dia == 2:
        arquivo = os.path.join(BASE_DIR, "audio", config["audios"]["quarta"])
        print(f"[{datetime.now().replace(microsecond=0)}] | Quarta | Sirene executada com sucesso.")
        log("Quarta")

    elif dia == 3:
        arquivo = os.path.join(BASE_DIR, "audio", config["audios"]["quinta"])
        print(f"[{datetime.now().replace(microsecond=0)}] | Quinta | Sirene executada com sucesso.")
        log("Quinta")

    elif dia == 4:
        arquivo = os.path.join(BASE_DIR, "audio", config["audios"]["sexta"])
        print(f"[{datetime.now().replace(microsecond=0)}] | Sexta | Sirene executada com sucesso.")
        log("Sexta")

    elif dia >= 5:
        print(f"[{datetime.now().replace(microsecond=0)}] | Final de semana | Execução ignorada.")
        return

    # Carrega e reproduz o arquivo de áudio correspondente ao dia atual.
    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.play()


def agendar_sinal(tocar):
    """
    Agenda todos os horários definidos no arquivo de configuração.

    Args:
        tocar (function): Função responsável pela reprodução da sirene.
    """

    for horario in config["horarios"]:
        schedule.every().day.at(horario).do(tocar)


# Registra todos os horários configurados.
agendar_sinal(tocar_semanal)

print("Aguardando horário programado...")

# Mantém a aplicação em execução realizando a verificação
# contínua das tarefas agendadas.
while True:
    schedule.run_pending()
    time.sleep(1)