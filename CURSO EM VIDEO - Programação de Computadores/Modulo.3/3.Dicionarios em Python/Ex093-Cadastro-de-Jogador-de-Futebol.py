jogador=dict()
gol=list()
jogador['Nome']=str(input("Nome do jogador: "))
qntd=int(input(f"Quantas partidas {jogador['Nome']} jogou: "))
for i in range(qntd):
    gol.append(int(input(f"Quantos gols na partida {i+1}?")))
jogador['Gols'] = gol[:]
jogador['Total'] = sum(gol)

print("=-="*10)
print(jogador)
print("=-="*10)
for k,v in jogador.items():
    print(f"{k}: {v}.")
print("=-="*10)
print(f"O jogador {jogador['Nome']} jogou {len(jogador['Gols'])} partidas.") 
for i,v in enumerate(jogador['Gols']):
    print(f"Na partida {i+1} fez {v} Gols.")
print(f"Foi um total de {jogador['Total']} Gols.")