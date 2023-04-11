import random
import re

global baralho, jogador, dealer,pontos
baralho = list()
jogador = list()
dealer = list()
pontos= [0,0]


def zerarBaralho():
    baralho.clear()
    jogador.clear()
    dealer.clear()
    baralho.extend(['|A  |\n|   |\n| ♣ |\n|   |\n|  A|',
                    '|2  |\n|   |\n| ♣ |\n|   |\n|  2|',
                    '|3  |\n|   |\n| ♣ |\n|   |\n|  3|',
                    '|4  |\n|   |\n| ♣ |\n|   |\n|  4|',
                    '|5  |\n|   |\n| ♣ |\n|   |\n|  5|',
                    '|6  |\n|   |\n| ♣ |\n|   |\n|  6|',
                    '|7  |\n|   |\n| ♣ |\n|   |\n|  7|',
                    '|8  |\n|   |\n| ♣ |\n|   |\n|  8|',
                    '|9  |\n|   |\n| ♣ |\n|   |\n|  9|',
                    '|10 |\n|   |\n| ♣ |\n|   |\n| 10|',
                    '|J  |\n|   |\n| ♣ |\n|   |\n|  J|',
                    '|Q  |\n|   |\n| ♣ |\n|   |\n|  Q|',
                    '|K  |\n|   |\n| ♣ |\n|   |\n|  K|',

                    '|A  |\n|   |\n| ♠ |\n|   |\n|  A|',
                    '|2  |\n|   |\n| ♠ |\n|   |\n|  2|',
                    '|3  |\n|   |\n| ♠ |\n|   |\n|  3|',
                    '|4  |\n|   |\n| ♠ |\n|   |\n|  4|',
                    '|5  |\n|   |\n| ♠ |\n|   |\n|  5|',
                    '|6  |\n|   |\n| ♠ |\n|   |\n|  6|',
                    '|7  |\n|   |\n| ♠ |\n|   |\n|  7|',
                    '|8  |\n|   |\n| ♠ |\n|   |\n|  8|',
                    '|9  |\n|   |\n| ♠ |\n|   |\n|  9|',
                    '|10 |\n|   |\n| ♠ |\n|   |\n| 10|',
                    '|J  |\n|   |\n| ♠ |\n|   |\n|  J|',
                    '|Q  |\n|   |\n| ♠ |\n|   |\n|  Q|',
                    '|K  |\n|   |\n| ♠ |\n|   |\n|  K|',

                    '|A  |\n|   |\n| ♥ |\n|   |\n|  A|',
                    '|2  |\n|   |\n| ♥ |\n|   |\n|  2|',
                    '|3  |\n|   |\n| ♥ |\n|   |\n|  3|',
                    '|4  |\n|   |\n| ♥ |\n|   |\n|  4|',
                    '|5  |\n|   |\n| ♥ |\n|   |\n|  5|',
                    '|6  |\n|   |\n| ♥ |\n|   |\n|  6|',
                    '|7  |\n|   |\n| ♥ |\n|   |\n|  7|',
                    '|8  |\n|   |\n| ♥ |\n|   |\n|  8|',
                    '|9  |\n|   |\n| ♥ |\n|   |\n|  9|',
                    '|10 |\n|   |\n| ♥ |\n|   |\n| 10|',
                    '|J  |\n|   |\n| ♥ |\n|   |\n|  J|',
                    '|Q  |\n|   |\n| ♥ |\n|   |\n|  Q|',
                    '|K  |\n|   |\n| ♥ |\n|   |\n|  K|',

                    '|A  |\n|   |\n| ♦ |\n|   |\n|  A|',
                    '|2  |\n|   |\n| ♦ |\n|   |\n|  2|',
                    '|3  |\n|   |\n| ♦ |\n|   |\n|  3|',
                    '|4  |\n|   |\n| ♦ |\n|   |\n|  4|',
                    '|5  |\n|   |\n| ♦ |\n|   |\n|  5|',
                    '|6  |\n|   |\n| ♦ |\n|   |\n|  6|',
                    '|7  |\n|   |\n| ♦ |\n|   |\n|  7|',
                    '|8  |\n|   |\n| ♦ |\n|   |\n|  8|',
                    '|9  |\n|   |\n| ♦ |\n|   |\n|  9|',
                    '|10 |\n|   |\n| ♦ |\n|   |\n| 10|',
                    '|J  |\n|   |\n| ♦ |\n|   |\n|  J|',
                    '|Q  |\n|   |\n| ♦ |\n|   |\n|  Q|',
                    '|K  |\n|   |\n| ♦ |\n|   |\n|  K|',
                    ])


def sortearCartas():
    jogador.clear()
    dealer.clear()
    c1 = random.randint(0, len(baralho) - 1)
    jogador.append(baralho[c1])
    baralho.pop(c1)
    c2 = random.randint(0, len(baralho) - 1)
    dealer.append(baralho[c2])
    baralho.pop(c2)
    c3 = random.randint(0, len(baralho) - 1)
    jogador.append(baralho[c3])
    baralho.pop(c3)
    c4 = random.randint(0, len(baralho) - 1)
    dealer.append(baralho[c4])
    baralho.pop(c4)



def pontuacao():
    ptjogador= 0
    ptdealer = 0

    for i in jogador:
        if re.search(".*A.*", i):
            if ptjogador + 11 > 21:
                ptjogador += 1
            else:
                ptjogador += 11
        elif re.search(".*J.*", i) or re.search(".*Q.*", i) or re.search(".*K.*", i):
            ptjogador += 10
        else:
            ptjogador += int(i[1:3])

    for j in dealer:
        if re.search(".*A.*", j):
            if ptdealer + 11 > 21:
                ptdealer += 1
            else:
                ptdealer += 11
        elif re.search(".*J.*", j) or re.search(".*Q.*", j) or re.search(".*K.*", j):
            ptdealer += 10
        else:
            ptdealer += int(j[1:3])

    pontos.insert(0,ptjogador)
    pontos.insert(1,ptdealer)


def hit():
    try:
        c1 = random.randint(0, len(baralho) - 1)
        jogador.append(baralho[c1])
        baralho.pop(c1)

        if(pontos[1]<17):
            c2 = random.randint(0, len(baralho) - 1)
            dealer.append(baralho[c2])
            baralho.pop(c2)
            pontuacao()
    except:
        pass

    pontuacao()


def stand():
    try:
        while (pontos[1]<17):
            c2 = random.randint(0, len(baralho) - 1)
            dealer.append(baralho[c2])
            baralho.pop(c2)
            pontuacao()
    except:
        pass

    pontuacao()


again = "S"
dinheiro = 100
while again =="S":
    while dinheiro>0:
        zerarBaralho()
        sortearCartas()
        pontuacao()

        while True:
            print(f"Dealer:\n")
            for index, i in enumerate(dealer):
                if index == 0:
                    print(f"|?  |\n|   |\n| ? |\n|   |\n|  ?|\n_____\n")
                else:
                    print(f"{i}\n")

            print(f"Jogador {pontos[0]}:")
            for i in jogador:
                print(i)
            while True:
                acao = input("Hit(H) Stand(S)? ").upper()
                if acao == "H" or acao == "S":
                    break
                print("Entrada inválida, por favor digite H ou S")
            if acao =="H":
                hit()
            elif acao=="S":
                stand()
                break

        pontuacao()
        print(f"Dealer:{pontos[1]}\n")
        for i in dealer:
            print(i)

        print(f"Jogador {pontos[0]}:")
        for i in jogador:
            print(i)


        if pontos[0]<=21 and pontos[1]<=21:
            if pontos[1]>pontos[0]:
                dinheiro-=10
                print(f"Voce Perdeu \n Total de Fichas: {dinheiro}")
            elif pontos[1]<pontos[0]:
                dinheiro+=10
                print(f"Voce Venceu \n Total de Fichas: {dinheiro}")
        elif pontos[0]>21:
            if pontos[1]>21:
                print(f"Ambos Estouraram \n Total de Fichas: {dinheiro}")
            else:
                dinheiro-=10
                print(f"Voce Perdeu \n Total de Fichas: {dinheiro}")
        elif pontos[1]>21:
            if pontos[0]>21:
                print(f"Ambos Estouraram \n Total de Fichas: {dinheiro}")
            else:
                dinheiro+=10
                print(f"Voce Venceu \n Total de Fichas: {dinheiro}")

        x = input("Proxima Rodada ou digite Sair")
        if x =="sair":
            break

    again = input("Jogar Novamente(S/N)?: ").upper()
