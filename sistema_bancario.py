def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
            
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
                
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
            
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    return saldo, extrato

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

    
def criar_cliente(usuarios):
    cpf = input("Digite o CPF: ")
    cpf_ja_cadastrado = [usuario["cpf"] == cpf for usuario in usuarios if usuario["cpf"] == cpf]

    if cpf_ja_cadastrado:
        print("Já existe usuario com este CPF")
        return
    nome = input("Digite o nome: ")
    data_nascimento = input("Digite data de nascimento (dd/mm/aaaa): ")
    endereco = input("Digite o endereco (logradouro, numero - bairro - cidade/sigla do estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})



def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF: ")
    usuario_cadastrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    if usuario_cadastrado:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario_cadastrado}
    print("Usuário não encontrado")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
    """





def main():

    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo usuário
    [q] Sair

    => """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)
            
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = saque(saldo= saldo, valor= valor, extrato= extrato, limite= limite,
                                   numero_saques= numero_saques, limite_saques= LIMITE_SAQUES) 

        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "nu":
            criar_cliente(usuarios)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")