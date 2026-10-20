def mais(x, y):
    return x + y

def menos(x, y):
    return x - y

def multi(x, y):
    return x * y

def divisao(x, y):
    return x / y


print("Olá, seja bem-vindo à mini calculadora!!")
opcao = input("Escolha entre as seguintes operações: Soma, Subtração, Multiplicação e Divisão.\n").strip().capitalize()

if opcao in ["Soma", "Subtração", "Multiplicação", "Divisão"]:
    try:
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))
        
        if opcao == "Soma":
            resultado = mais(x, y)
            print(f"A soma de {x} e {y} é {resultado}.")
        elif opcao == "Subtração":
            resultado = menos(x, y)
            print(f"A subtração de {x} e {y} é {resultado}.")
        elif opcao == "Multiplicação":
            resultado = multi(x, y)
            print(f"A multiplicação de {x} e {y} é {resultado}.")
        elif opcao == "Divisão":
            if y == 0:
                print("Erro... Não é possível dividir por zero.")
            else:
                resultado = divisao(x, y)
                print(f"A divisão de {x} e {y} é {resultado}.")
                
    except ValueError:
        print("Erro: Digite apenas números válidos!!")
else:
    print("Erro... Operação inválida. Escolha entre as opções anteriores.")