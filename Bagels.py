# Pico      Um digito correto, mas posição errada
# Fermi     Um digito correto, e nao posição correta
# Bagels    Nenhum digito correto

import random

again = "S"
while again == "S":
    numero = list(str(random.randint(1, 999)).zfill(3))

    for i in range(0, 10):
        palpite = list(str(input("Digite um numero: ")).zfill(3))
        if palpite == numero:
            print("Parabens, voce adivinhou!!")
            i = "V"
            break
        if (palpite[0] not in numero and palpite[1] not in numero and palpite[2] not in numero) and i != 9:
            print("Bagels")
        elif i != 9:
            if palpite[0] in numero:
                if palpite[0] == numero[0]:
                    print("Fermi")
                else:
                    print("Pico")
            if palpite[1] in numero:
                if palpite[1] == numero[1]:
                    print("Fermi")
                else:
                    print("Pico")
            if palpite[2] in numero:
                if palpite[2] == numero[2]:
                    print("Fermi")
                else:
                    print("Pico")

    if i == "V":
        again = input("Jogar Novamente (S/N)?").upper()
    else:
        print("Voce perdeu!!")
        again = input("Jogar Novamente (S/N)?").upper()
