# 15. Uso dos Módulos os, time, datetime e calendar
# Crie um programa que:
# • Exibe o diretório atual usando os.getcwd().
# • Exibe a data e a hora atuais usando datetime.datetime.now().
# • Exibe o calendário do mês atual usando calendar.month().
# • Faz uma pausa de 3 segundos usando time.sleep(3).

import os
import time
import datetime
import calendar

print(f"Diretório atual: {os.getcwd()}")

print(f"Data e hora atuais: {datetime.datetime.now()}")

mes_atual = datetime.datetime.now().month
print(f"Calendário do mês atual:\n{calendar.month(datetime.datetime.now().year, mes_atual)}")

print("Pausando por 3 segundos...")
time.sleep(3)
print("Pausa concluída.")
