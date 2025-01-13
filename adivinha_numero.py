import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas = 0
    max_tentativas = 3

    print("Bem-vindo ao jogo de adivinhação! \n")
    print("Estou pensando em um número entre 1 e 10. \n")
    print(f"Você tem {max_tentativas} tentativas para adivinhar.")

    while tentativas < max_tentativas:
        palpite = int(input("Faça um palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo!")
        elif palpite > numero_secreto:
            print("Muito alto!")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            break

    if tentativas == max_tentativas and palpite != numero_secreto:
        print(f"Suas tentativas acabaram! O número secreto era {numero_secreto}. Melhor sorte na próxima vez.")


jogo_adivinhacao()
