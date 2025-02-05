menu = """
    [D] - Depositar
    [S] - Sacar
    [E] - Extrato
    [Q] - Sair
"""

balance: float = 0
limit: float = 500
bank_statement: str = ""
withdrawal_quantity: int = 0
WITHDRAWAL_LIMIT: int = 3

while True:
    option = input(menu)

    if option == "D":
        value = float(input("Digite o valor a ser depositado: "))

        if value <= 0:
            print("Valor inválido, por favor insira um valor válido.")
        else:
            balance += value
            bank_statement += f"Depósito: R$ {value:.2f}\n"

    elif option == "S":
        value = float(input("Digite o valor a ser sacado: "))

        withdrawal_exceeded = value > balance

        limit_exceeded = value > limit

        withdrawal_limit_exceeded = withdrawal_quantity > WITHDRAWAL_LIMIT

        if withdrawal_exceeded:
            print("Operação falhou! Você não tem saldo suficiente")

        elif limit_exceeded:
            print("Operação falhou! Você excedeu o limite de valor para saque.")

        elif withdrawal_limit_exceeded:
            print("Operação falhou! Você excedeu limite de saques.")

        elif value > 0:
            balance -= value
            bank_statement += f"Saque: R$ {value:.2f}\n"
            withdrawal_quantity += 1

    elif option == "E":
        print("Extrato:\n")
        print(bank_statement)
        print(f"Saldo atual: R$ {balance:.2f}\n")

    elif option == "Q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
