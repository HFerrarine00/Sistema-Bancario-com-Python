import textwrap  # Importa o módulo textwrap para lidar com formatação de texto

# Define a função 'exibir_menu' que mostra o menu e recebe a escolha do usuário
def exibir_menu():
    menu_texto = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_texto))

# Define a função 'fazer_deposito' para realizar depósitos
def fazer_deposito(saldo_atual, valor, historico, /):
    if valor > 0:
        saldo_atual += valor
        historico += f"Depósito:\tR$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo_atual, historico

# Define a função 'fazer_saque' para realizar saques
def fazer_saque(*, saldo_atual, valor, historico, limite, num_saques, limite_saques):
    saldo_insuficiente = valor > saldo_atual
    excedeu_limite = valor > limite
    excedeu_num_saques = num_saques >= limite_saques

    if saldo_insuficiente:
        print("\n@@@ Operação falhou! Saldo insuficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! Valor do saque excede o limite. @@@")

    elif excedeu_num_saques:
        print("\n@@@ Operação falhou! Número máximo de saques atingido. @@@")

    elif valor > 0:
        saldo_atual -= valor
        historico += f"Saque:\t\tR$ {valor:.2f}\n"
        num_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! Valor inválido. @@@")

    return saldo_atual, historico

# Define a função 'mostrar_historico' para exibir o histórico de transações
def mostrar_historico(saldo_atual, /, *, historico):
    print("\n================ HISTÓRICO ================")
    print("Nenhuma transação realizada." if not historico else historico)
    print(f"\nSaldo:\t\tR$ {saldo_atual:.2f}")
    print("===========================================")

# Define a função 'criar_novo_usuario' para adicionar um novo usuário
def criar_novo_usuario(lista_usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = buscar_usuario(cpf, lista_usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    lista_usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

# Define a função 'buscar_usuario' para procurar um usuário pelo CPF
def buscar_usuario(cpf, lista_usuarios):
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Define a função 'criar_nova_conta' para criar uma nova conta
def criar_nova_conta(agencia, num_conta, lista_usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = buscar_usuario(cpf, lista_usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "num_conta": num_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, criação de conta encerrada! @@@")

# Define a função 'listar_contas' para exibir informações das contas
def listar_contas(lista_contas):
    for conta in lista_contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['num_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

# Função principal do programa
def executar_programa():
    LIMITE_SAQUES = 3
    AGENCIA_PADRAO = "0001"

    saldo_atual = 0
    limite_saque = 500
    historico_transacoes = ""
    num_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo_atual, historico_transacoes = fazer_deposito(saldo_atual, valor, historico_transacoes)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo_atual, historico_transacoes = fazer_saque(
                saldo_atual=saldo_atual,
                valor=valor,
                historico=historico_transacoes,
                limite=limite_saque,
                num_saques=num_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            mostrar_historico(saldo_atual, historico=historico_transacoes)

        elif opcao == "nu":
            criar_novo_usuario(usuarios)

        elif opcao == "nc":
            num_conta = len(contas) + 1
            conta = criar_nova_conta(AGENCIA_PADRAO, num_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida. Selecione novamente a operação desejada.")

# Chama a função principal para iniciar o programa
executar_programa()
