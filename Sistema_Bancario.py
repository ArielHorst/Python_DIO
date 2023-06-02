                                        # SISTEMA BANCÁRIO

# Personalizar o script:

cores = {'limpa':'\033[m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m'}

frase = 'CAIXA ELETRÔNICO DIO'
print(f'{cores["amarelo"]}=-={cores["limpa"]}'*15)
print(f'{cores["azul"]}{frase:^42}{cores["limpa"]}')
print(f'{cores["amarelo"]}=-={cores["limpa"]}'*15)
boasvindas = 'BEM-VINDO !'
print(f'{cores["verde"]}{boasvindas:^44}{cores["limpa"]}')
print()


# Início do Script:

# - Imporatanto pacotes:
from datetime import datetime,timedelta

# - Criando/Inicionando variáveis e listas:
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

# Início do laço de repetição do menu !
while True:
    # Mostrar Intro:
    intro = 'Escolha uma das opções abaixo:'
    print('-' * 45)
    print(f'{intro:^43}')

    # Validar/Mostrar as escolhas do menu:
    while True:
        print('-' * 45)
        choice = int(input(f'{"[1].Depósito":^40}'
                           f'\n{"[2].Saque":^38}'
                           f'\n{"[3].Extrato":^40}'
                           f'\n{"[4].Sair":^37}'
                           f'\nEscolha: '))
        # Deve estar entre 1<-->4:
        if (choice < 1) or (choice > 4):
            print(f'{cores["vermelho"]}ERRO!{cores["limpa"]} '
                  f'Por favor, informe uma opção válida.')
        else:
            break
        # Fim da validação
    print('')

    # Após validar a opção informada...

    #  - Caso seja selecionada a opção 1:
    if choice == 1:
        # Validação simples de dados de entrada:
        while True:
            print(f'DEPÓSITO')
            print('')
            print(f'** Para voltar ao menu, digite {cores["amarelo"]}'
                  f'0.1{cores["limpa"]} **')
            print('')
            value_dep = float(input('Informe o valor do depósito (R$): '))

            if value_dep <= 0:
                print(f'{cores["vermelho"]}ERRO!{cores["limpa"]} '
                      f'Por favor, informe um valor maior do que R$ 0.00 .')
                print('')
            elif value_dep == 0.1:
                break
            # Fim da Validação.
            else:
                # INÍCIO ----> Script para a opção 1 - Depósito
                value_saldo += value_dep
                temp_dict['date'] = present_day.strftime('%d/%m/%Y')
                temp_dict['deposito'] = value_dep
                depositos_list.append(temp_dict.copy())
                temp_dict.clear()
                print('')
                print(f'O valor de {cores["verde"]}R$ {value_dep:.2f}{cores["limpa"]} foi depositado'
                      f' em sua conta.')
                break
                # FIM ----> Script para a opção 1 - Depósito

    #  - Caso seja selecionada a opção 2:
    elif choice == 2:
        while True:
            print(f'SAQUE')
            print('-'*40)
            print(f'Data de Hoje:', present_day.strftime('%d/%m/%Y'))
            print('_'*40)
            print(f'** Para voltar ao menu, digite {cores["amarelo"]}'
                  f'0.1{cores["limpa"]} **')
            print()
            saque = float(input('Informe o valor do saque (R$): '))
            # Caso o número de saques seja superior a 3
            if numbers_saque > 3:
                print(f'{cores["vermelho"]}ERRO!{cores["limpa"]} '
                      f'O máximo de saques permitidos por dia são {cores["amarelo"]}3{cores["limpa"]}.'
                      f'\nA partir do dia {cores["verde"]}{tomorrow.strftime("%d/%m/%Y")}{cores["limpa"]}'
                      f', você poderá realizar mais operações de saque.')
                print('')
            # Caso o valor do saque seja menor ou igual a zero:
            elif saque <= 0:
                print(f'{cores["vermelho"]}ERRO!{cores["limpa"]} '
                      f'Por favor, informe um valor positivo e maior do que zero !')
                print('')
            # Caso o saque seja maior que o saldo em conta:
            elif saque > value_saldo:
                print(f'{cores["vermelho"]}ATENÇÃO!{cores["limpa"]} '
                      f'Não há valor suficiente em conta para realizar o saque !')
                print('_'*10)
                print(f'O Seu saldo atual é: {cores["verde"]}R$ {value_saldo:.2f}{cores["limpa"]} .')
                print('')
            # Caso o cliente queira voltar ao menu principal:
            elif saque == 0.1:
                break
            # Caso em que o saque é permitido:
            else:
                value_saldo -= saque
                numbers_saque += 1
                temp_dict['date'] = present_day.strftime('%d/%m/%Y')
                temp_dict['saque'] = saque
                saques_list.append(temp_dict.copy())
                temp_dict.clear()
                print(f'O Saque no valor de {cores["verde"]}R$ {saque:.2f}{cores["limpa"]} foi permitido'
                      f' e efetuado com sucesso.')
                break

    #  - Caso seja selecionada a opção 3:
    elif choice == 3:
        print(' EXTRATO '.center(45,'#'))
        print()

        # Caso exista somente o valor do saldo
        if len(depositos_list) == 0 and len(saques_list) == 0:
            print('Não foram encontradas '
                  '\ntransações em sua conta.')

        # Caso existam somente depositos
        elif len(depositos_list) > 0 and len(saques_list) == 0:
            print('Não foram encontradas transações '
                  '\nde SAQUE em sua conta.')
            print()
            print(f'{cores["azul"]}')
            print(f' {cores["azul"]}DEPÓSITOS '.center(52, '-'))
            print()
            for i in range(len(depositos_list)):
                print(f'{cores["limpa"]}Data: {depositos_list[i]["date"]}', end='')
                print(f'            Valor: R$ {depositos_list[i]["deposito"]:.2f}')
            print()

        # Caso existam somente saques
        elif len(saques_list) > 0 and len(depositos_list) == 0:
            print('Não foram encontradas transações '
                  '\nde DEPÓSITOS em sua conta.')
            print()
            print(f'{cores["azul"]}')
            print(f' {cores["azul"]}SAQUES '.center(52, '-'))
            print()
            for i in range(len(saques_list)):
                print(f'{cores["limpa"]}Data: {saques_list[i]["date"]}', end='')
                print(f'            Valor: R$ {saques_list[i]["saque"]:.2f}')
            print()
        # Caso existam informações completas:
        else:
            # Mostrar o extrato completo da conta do cliente:

            # - Primeiro, mostrar os depósitos:
            print(f'{cores["azul"]}')
            print(f' {cores["azul"]}DEPÓSITOS '.center(52,'-'))
            print()
            for i in range(len(depositos_list)):
                print(f'{cores["limpa"]}Data: {depositos_list[i]["date"]}', end='')
                print(f'            Valor: R$ {depositos_list[i]["deposito"]:.2f}')

            # - Em seguida, mostrar os saques:
            print(f'{cores["azul"]}')
            print(f' {cores["azul"]}SAQUES '.center(52, '-'))
            print()
            for i in range(len(saques_list)):
                print(f'{cores["limpa"]}Data: {saques_list[i]["date"]}', end='')
                print(f'             Valor: R$ {saques_list[i]["saque"]:.2f}')
            print()

        # - Mostar o saldo atual da conta, após todas as operações
        print(f'{cores["azul"]}-{cores["limpa"]}' * 45)
        print()
        print(f'[SALDO]: {cores["verde"]}R$ {value_saldo:.2f}{cores["limpa"]}')
        print()

    #  - Caso seja selecionada a opção 4...
    # Saída do laço de repetição do Menu (opção [4]):
    else:
        break

# Fim do script
print()
frase = 'CAIXA ELETRÔNICO DIO'
print(f'{cores["amarelo"]}=-={cores["limpa"]}'*15)
print(f'{cores["azul"]}{frase:^42}{cores["limpa"]}')
print(f'{cores["amarelo"]}=-={cores["limpa"]}'*15)
despedida = 'OBRIGADO, VOLTE SEMPRE !'
print(f'{cores["verde"]}{despedida:^44}{cores["limpa"]}')












