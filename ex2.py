"""-*-*-*-*-*-*-*-*-Média aritmética-*-*-*-*-*-*-*-*"""
n1 = input("Digite sua 1ª Nota: ")
n2 = input("Digite sua 1ª Nota: ")
n3 = input("Digite sua 1ª Nota: ")


media = n1 + n2 + n3 
resultado = media / 3 
print(f"Você ficou com a nota: " + resultado)


if (media >= 7):
    print("Você foi aprovado!")
else:
    print("Você foi retido!")

