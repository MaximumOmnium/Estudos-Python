print("Olá, seja bem-vindo à calculadora de decimais e binários!")
print()
print("Por favor, selecione uma das opções:")
print("1 - Decimal para Binário")
print("2 - Binário para Decimal")
print()

opcao = input("Digite sua opção (1/2): ").strip()

if opcao == "1":
    numero = input("Digite um número decimal positivo: ").strip()
    if numero.isdigit():
        decimal = int(entrada)
        binario = bin(decimal)[2:]
        print(f"O número {decimal} em binário é {binario}.")
    else:
        print("Erro... Por favor, insira apenas números inteiros positivos válidos.")

elif opcao == "2":
    binario = input("Digite um número binário: ").strip()
    try:
        decimal = int(binario, 2)
        print(f"O número binário {binario} em decimal é {decimal}.")
    except ValueError:
        print("Erro... Por favor, insira um número binário válido.")

else:
    print("Erro... Opção inválida. Por favor, escolha 1 ou 2.")