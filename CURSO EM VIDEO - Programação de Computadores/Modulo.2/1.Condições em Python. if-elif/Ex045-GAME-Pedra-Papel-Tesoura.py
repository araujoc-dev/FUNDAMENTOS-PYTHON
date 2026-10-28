import random
escolhas= ("Pedra","Papel","Tesoura")
pc=random.randint(1,3)
print("Suas opcões:\n[1] Pedra.\n[2] Papel.\n[3] Tesoura.")
jogador=int(input("Qual é a sua jogada? "))
print(f"{"=-=" * 6}\nPC Jogou: {escolhas[pc-1]}\nVocê jogou: {escolhas[jogador-1]}\n{"=-=" * 6}")
if pc == 1: #pedra
    if jogador == 1:
        print("Empate")
    elif jogador == 2:
        print("Jogador Ganhou!")
    elif jogador == 3: 
        print("PC Ganhou!")
    else:
        print("Jogada Inválida")
elif pc == 2: #papel
    if jogador == 1:
        print("PC Ganhou!")
    elif jogador == 2:
        print("Empate")
    elif jogador == 3:
        print("Jogador Ganhou!")
    else:
        print("Jogada Inválida")
elif pc == 3: #tesoura
    if jogador == 1:
        print("Jogador Ganhou!")
    elif jogador == 2:
        print("PC Ganhou!")
    elif jogador == 3: 
        print("Empate")
    else:
        print("Jogada Inválida")