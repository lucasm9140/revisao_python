import random

# Loop - Repetição - Laço de repetição
while True:
    numero_aleatorio = random.randint(1,25)
    print(f"Número sorteado: {numero_aleatorio}")
    resposta = input("Deseja sortear outro número? (s/n)").strip().lower()
    if resposta == 'n':
        print("Encerrando o sorteio!")
        break