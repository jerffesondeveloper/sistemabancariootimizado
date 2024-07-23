import textwrap
from colorama import Fore, Back, Style

# INÍCIO DO CÓDIGO

def menu():
    menu = Fore.YELLOW +"""
    \n
    ================ MENU ================
    [d] \tDepositar
    [s] \tSacar
    [e] \tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [lu]\tListar usuário
    [q] \tSair
    => """ + Fore.RESET
    return input(textwrap.dedent(menu)).upper()

# FUNÇÕES

def depositar( valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR$ {valor:.2f}\n"
        print(Fore.BLUE + Back.LIGHTBLACK_EX + '\nDEPÓSITO REALIZADO COM SUCESSO!'+ Back.RESET + Fore.RESET)

    else:
        print(Fore.RED + Back.GREEN +"\nOperação falhou! O valor informado é inválido." + Fore.RESET + Back.RESET)
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques  

    if excedeu_saldo:
        print(Fore.RED + Back.GREEN +"\nVocê não tem saldo suficiente." + Fore.RESET + Back.RESET)

    elif excedeu_limite:
        print(Fore.RED + Back.GREEN +"\nO valor do saque excede o limite." + Fore.RESET + Back.RESET)
 
    elif excedeu_saques:
        print(Fore.RED + Back.GREEN +"\nNúmero máximo de saques excedido." + Fore.RESET + Back.RESET)

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:  \tR$ {valor:.2f}\n"
        numero_saques += 1
        print(Back.LIGHTBLACK_EX + Fore.LIGHTBLUE_EX +  '\nSAQUE REALIZADO COM SUCESSO!' + Fore.RESET + Back.RESET)
    else:
        print(Back.RED + Fore.YELLOW + 'OPÇÃO INVÁLIDA, TENTE NOVAMNETE'+ Back.RESET + Fore.RESET)

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato,):
    print(Style.BRIGHT + Fore.GREEN + Back.WHITE + '=================EXTRATO=================' + Style.RESET_ALL + Back.RESET + Fore.RESET )
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print(Style.BRIGHT + Fore.GREEN + Back.WHITE + "========================================="+ Style.RESET_ALL + Fore.RESET + Back.RESET)

def criar_usuario(usuarios):
    cpf = input("Informe o número (somente números) do CPF: ")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario: 
        print(Fore.GREEN + 'Usuario já cadastrado neste CPF!')
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(Fore.GREEN + "\nUsuário cadastrado com sucesso!" + Fore.RESET)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(Fore.GREEN + '\nCONTA CRIADA COM SUCESSO' + Fore.RESET)
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuarios': usuario}
    print(Fore.BLACK + Back.RED + '\n===========ATENÇÃO==========' + Fore.RESET + Back.RESET)
    print(Fore.RED + Back.GREEN + '''\n
Usuário não cadastrado!
Primeiro é preciso cadastrar o usuário!''' + Fore.RESET + Back.RESET)

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuarios']['nome']}
        """
    print("=" * 32)
    print(textwrap.dedent(Back.RED + Fore.BLACK + '\nAinda não há contas cadastradas!' + Back.RESET + Fore.RESET if not contas else linha))
    # print(Back.RED + Fore.BLACK + '\nAinda não há contas cadastradas!'+ Back.RESET + Fore.RESET)

def listar_usuario(usuarios):
    for usuario in usuarios:
        linha_2 = f'''\
            Nome:\t\t{usuario['nome']}
            CPF:\t\t{usuario['cpf']}
            Aniversário:\t{usuario['data_nascimento']}
            Endereço:\t{usuario['endereco']}
        '''
    print("=" * 34)
    print(textwrap.dedent(Back.RED + Fore.BLACK + '\nAinda não há usuários cadastrados!' + Back.RESET + Fore.RESET if not usuarios else linha_2))
    # print(Back.RED + Fore.BLACK + '\nAinda não há usuários cadastrados!'+ Back.RESET + Fore.RESET)


# FUNÇÃO PRINCIPAL - CHAMA AS OUTRAS 
def main():
    
    AGENCIA = "0001"
    limite_saques = 3
    saldo = 0
    limite = 1000
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    operador = ('JERFFESON')
    senha = ('1234')

# Senha para entrar 
    
    while True:
        login = input(Back.WHITE + Fore.BLACK + Style.BRIGHT + '''\nDIGITE SUA SENHA DE ACESSO:=> '''+ Back.RESET + Fore.RESET + Style.RESET_ALL).upper()
        if login == senha:
            print(Back.GREEN + Style.BRIGHT + '''\nBem vindo, {}'''.format(operador) + Back.RESET + Style.BRIGHT)
            break
        else:
            print(Fore.RED + '\nSenha incorreta!'+ Fore.RESET)

    while True:
        opcao = menu()

        if opcao == "D":
            valor = float(input(Fore.GREEN + 'Informe o valor para depósito: '))
            saldo, extrato = depositar(valor, saldo, extrato)

        elif opcao == "S":
            
            valor = float(input(Fore.GREEN + '\nInforme o valor do saque: \n' + Fore.RESET))
            
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques)
            
        elif opcao == "E":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao =="NU":
            criar_usuario(usuarios)

        elif opcao == "NC":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        
        elif opcao == "LC":
            listar_contas(contas)

        elif opcao == "LU":
            listar_usuario(usuarios)     

        elif opcao == "Q":
            print('OPERAÇÃO ENCERRADA!')
            break

        else:
            print(Back.RED + Fore.YELLOW + 'OPÇÃO INVÁLIDA, TENTE NOVAMNETE'+ Back.RESET + Fore.RESET) 


main()

