import time, os, sys

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

limpar_tela()

typingPrint("Olá, seja bem-vindo ao quiz de Cibersegurança!\n")
time.sleep(1)
typingPrint("O quiz é composto por 10 questões, valendo 1 ponto cada.\n")
time.sleep(1)
typingPrint("Portanto, cuidado para não errar nenhuma!\n")
time.sleep(1)
typingPrint("Boa sorte! ;)\n")
time.sleep(1)
typingPrint("....\n")
time.sleep(1)

question_prompts = [
    "Qual das opções abaixo é uma linguagem de programação?\n(A) VS Code\n(B) print\n(C) Python\n(D) HTML",
    "Qual comando em Python exibe algo na tela?\n(A) echo\n(B) print()\n(C) console.log()\n(D) write()",
    "O que é um phishing?\n(A) Um tipo de vírus\n(B) Um ataque de engenharia social\n(C) Um firewall\n(D) Um protocolo de rede",
    "Qual símbolo é usado para comparação de igualdade em Python?\n(A) =\n(B) ==\n(C) ===\n(D) !=",
    "Qual destes NÃO é um sistema operacional?\n(A) Linux\n(B) Windows\n(C) Android\n(D) Google Chrome",
    "Em Python, qual operador é usado para multiplicação?\n(A) X\n(B) *\n(C) /\n(D) %",
    "O que acontece se você tentar dividir um número por zero em Python?\n(A) O resultado será zero\n(B) O programa exibirá um erro\n(C) O resultado será infinito\n(D) O Python corrigirá automaticamente para 1",
    "Qual é a extensão padrão de um arquivo Python?\n(A) .py\n(B) .java\n(C) .python\n(D) .cpp",
    "O que significa o operador lógico and em Python?\n(A) Retorna verdadeiro se pelo menos uma condição for verdadeira\n(B) Retorna verdadeiro apenas se todas as condições forem verdadeiras\n(C) Retorna verdadeiro apenas se todas as condições forem falsas\n(D) Não possui função em Python",
    "Qual das opções abaixo é um exemplo de um tipo de dado booleano?\n(A) Texto\n(B) 100\n(C) True\n(D) 3.14"
]

questions = [
    Question(question_prompts[0], "C"),
    Question(question_prompts[1], "B"),
    Question(question_prompts[2], "B"),
    Question(question_prompts[3], "B"),
    Question(question_prompts[4], "D"),
    Question(question_prompts[5], "B"),
    Question(question_prompts[6], "B"),
    Question(question_prompts[7], "A"),
    Question(question_prompts[8], "B"),
    Question(question_prompts[9], "C")    
]

def run_quiz(questions):
    score = 0
    for i, question in enumerate(questions, 1):
        limpar_tela()
        typingPrint(f"Questão {i} de {len(questions)}\n\n")
        
        answer = input(question.prompt + "\nSua resposta (A/B/C/D): ").strip().upper()
        
        if answer == question.answer:
            typingPrint("\nResposta Correta!\n")
            score += 1
        else:
            typingPrint(f"\nResposta Incorreta! Alternativa correta: ({question.answer})\n")
            
        time.sleep(1.5)
        
    limpar_tela()
    typingPrint("Processando...\n")
    time.sleep(2)
    typingPrint(f"Você conseguiu {score}/{len(questions)} pontos.\n")
    
run_quiz(questions)
