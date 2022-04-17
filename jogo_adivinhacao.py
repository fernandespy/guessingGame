import random

rand = random.randint(1, 100)

attempt = 10

print('Bem vindo ao Jogo de Adivinhação!!')
print('Escolha um número e tente a sorte!! Precisa ser um número entre 1 e 100')

while True:
    number_one = int(input("Digite o número escolhido: "))

    if number_one == rand:
        print(" Parabéns você acertou! ")
        break

    elif number_one > rand:
        print("O número que você chutou foi maior! ")

    elif number_one < rand:
        print("O número chutado foi menor! ")

    elif attempt == 0:
        print('Acabou suas tentativas! Tente de novo!')
        break 

    attempt -= 1
    print(f" numero restante de tentativas", +attempt)