import random
# Iniciar Variavel para o Loop
newGame = "Y"

# Loop para repetir o jogo
while (newGame == "Y"):
    # Iniciar Variavel para o Loop
    Eu = ''
    # Loop para tratamento de Input
    while (Eu != "R") and (Eu != "P") and (Eu != "S"):
        # Tratando o Case Sensitive do Python, deixando tudo Upper Case
        Eu = input("JO-KEN-PO(R = rock, P = Paper, S = Scissors): ").upper()
        # Caso o valor digitado seja válido, se encerra o Loop
        if (Eu == "R") or (Eu == "P") or (Eu == "S"):
            break
        #Caso o usuário não selecione um valor válido, mensagem e reinicia o loop de tratamento
        else:
            print("Selecione um dos valores válidos!!")

    # Lista para randomização
    myList = ['R', 'P', 'S']

    # Randomizando escolha da máquina
    Maq = random.choice(myList)

    # Lógica do jogo
    if Eu == Maq:
        print("Empatou!!")
    elif (Eu == "R" and Maq == "P") or (Eu == "P" and Maq == "S") or (Eu == "S" and Maq == "R"):
        print("Voce Perdeu!!")
    elif (Eu == "R" and Maq == "S") or (Eu == "P" and Maq == "R") or (Eu == "S" and Maq == "P"):
        print("Voce Ganhou!!")

    # Aqui o usuário decide jogar novamente ou não
    newGame = "N"
    while (newGame != "Y"):
        # Tratando o Case Sensitive do Python, deixando tudo Upper Case
        newGame = input("Jogar Novamente (Y/N)? ").upper()
        # Caso o valor digitado seja válido, se encerra o Loop
        if (newGame == "Y") or (newGame == "N"):
            break
        # Caso o usuário não selecione um valor válido, mensagem e reinicia o loop de tratamento
        else:
            print("Selecione um dos valores válidos!!")