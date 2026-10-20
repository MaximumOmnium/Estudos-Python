print("Direi se o seu número é PAR ou ÍMPAR.")

try:
    numero = int(input("Digite o número: "))
    
    if numero % 2 == 0:
        print("O número é par!")
    else:
        print("O número é ímpar!")
        
except ValueError:
    print("Erro... Por favor, insira apenas um número inteiro válido.")