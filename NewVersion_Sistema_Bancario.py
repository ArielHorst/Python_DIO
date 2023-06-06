                                        # Nova versão do SISTEMA BANCÁRIO 
# Início do Script:

# - Importanto pacotes:
from datetime import datetime,timedelta

# - Criando/Iniciando variáveis e listas:
present_day = datetime.now()
tomorrow = present_day + timedelta(1)
depositos_list = []
saques_list = []
temp_dict = {}
value_saldo = 0.0
value_dep = 0.0
numbers_saque = 1

# Laço de repetição para o valor inicial do saldo da conta:
while True:
    # Perguntar ao usuário se deseja definir o valor do saldo:
    answer = input(f'Deseja informar o valor do saldo em conta ?\n{cores["verde"]}[S]{cores["limpa"]}'
                   f'/{cores["vermelho"]}[N]{cores["limpa"]}\nInforme a opção desejada: ')
    # Se a resposta for 'SIM'
    if answer in 'Ss':
        print()
        value_saldo = float(input('Informe o valor do saldo inicial da conta (R$): '))
        break
    # Se a resposta for 'NÃO'
    elif answer in 'Nn':
        print()
        value_saldo = 3000.0
        print(f'O sistema definiu um saldo inicial igual a: '
              f'{cores["verde"]}R$ {value_saldo:.2f}{cores["limpa"]} .')
        break
    else:
        print('Por favor, informe uma opção válida.')
        print()
# Fim do laço de repetição










