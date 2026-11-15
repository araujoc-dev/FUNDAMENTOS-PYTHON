time=list()
jogador=dict()
gol=list()

while True:
    jogador.clear()
    jogador['Nome']=str(input("Nome do jogador: "))
    qntd=int(input(f"Quantas partidas {jogador['Nome']} jogou: "))
    gol.clear()
    for i in range(qntd):
        gol.append(int(input(f"Quantos gols na partida {i+1}?")))
    jogador['Gols'] = gol[:]
    jogador['Total'] = sum(gol)
    time.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar? [S/ N] ")).upper()[0]
        if resp in 'SN':
            break
        print("Erro! Responda SIM ou NÃO.")
    if resp == 'N':
        break
print("=-="*10)
print("cod",end='')
for i in jogador.keys():
    print(f"{i:<15}",end='')
print("=-="*10)
for k,v in enumerate(time):
    print(f"{k:>3} ", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print("=-="*10)
while True:
    busca = int(input("Mostrar dados de qual jogador? [999] PARAR! "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO! Não existe jogador com código {busca}!")
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:")
        for i, g in enumerate(time[busca]['Gols']):
            print(f"    No jogo {i+1} fez {g} Gols")
    print("=-="*10)
print("== VOLTE SEMPRE ==")