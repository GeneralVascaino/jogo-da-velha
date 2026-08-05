# Jogo da Velha Simples

tabuleiro = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

jogador = "X"

while True:

    print()
    print(tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
    print("--+---+--")
    print(tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
    print("--+---+--")
    print(tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])
    print()

    posicao = int(input(f"Jogador {jogador}, escolha uma posição (1-9): "))

    if tabuleiro[posicao - 1] == "X" or tabuleiro[posicao - 1] == "O":
        print("Essa posição já está ocupada!")
        continue

    tabuleiro[posicao - 1] = jogador

    # Verifica vitória
    if (
        (tabuleiro[0] == tabuleiro[1] == tabuleiro[2]) or
        (tabuleiro[3] == tabuleiro[4] == tabuleiro[5]) or
        (tabuleiro[6] == tabuleiro[7] == tabuleiro[8]) or
        (tabuleiro[0] == tabuleiro[3] == tabuleiro[6]) or
        (tabuleiro[1] == tabuleiro[4] == tabuleiro[7]) or
        (tabuleiro[2] == tabuleiro[5] == tabuleiro[8]) or
        (tabuleiro[0] == tabuleiro[4] == tabuleiro[8]) or
        (tabuleiro[2] == tabuleiro[4] == tabuleiro[6])
    ):
        print()
        print(tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
        print("--+---+--")
        print(tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
        print("--+---+--")
        print(tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])
        print()
        print(f"Jogador {jogador} venceu!")
        break

    # Verifica empate
    if "1" not in tabuleiro and "2" not in tabuleiro and "3" not in tabuleiro and \
       "4" not in tabuleiro and "5" not in tabuleiro and "6" not in tabuleiro and \
       "7" not in tabuleiro and "8" not in tabuleiro and "9" not in tabuleiro:
        print("Empate!")
        break

    # Troca o jogador
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"