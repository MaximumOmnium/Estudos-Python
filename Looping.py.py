import itertools
import time

caracteres = "abcdefghijklmnopqrstuvwxyz0123456789"
senha = input("Senha de no máximo 5 caracteres: ").strip().lower()

if len(senha) > 5 or len(senha) == 0:
    print("Erro A senha deve ter entre 1 e 5 caracteres!")
else:
    print(f"\nProcurando por '{senha}'.")
    print("Isso pode levar alguns segundos\n")
    
    tentativas = 0
    encontrou = False
    
    inicio = time.time()
    
    for tamanho in range(1, len(senha) + 1):
        for combinacao in itertools.product(caracteres, repeat=tamanho):
            tentativa = "".join(combinacao)
            tentativas += 1
            
            if tentativa == senha:
                fim = time.time()
                tempo_gasto = fim - inicio
                
                print("="*30)
                print(f"A senha foi encontrada em {tentativas} tentativas.")
                print(f"O tempo gasto foi de {tempo_gasto:.2f} segundos.")
                print("="*30)
                
                encontrou = True
                break
        if encontrou:
            break