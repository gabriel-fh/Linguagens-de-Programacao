# 2. Uso do Módulo platform
# Crie um programa que exiba informações sobre o sistema operacional usando o módulo
# platform. O programa deve imprimir:
# • Nome do sistema operacional
# • Versão do sistema
# • Arquitetura do processador

import platform

print(f"Sistema Operacional: {platform.system()}")
print(f"Versão do Sistema: {platform.version()}")
print(f"Arquitetura do Processador: {platform.architecture()[0]}")
