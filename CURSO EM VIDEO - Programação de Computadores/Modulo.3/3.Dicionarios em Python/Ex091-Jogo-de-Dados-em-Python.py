from random import randint
from time import sleep
from operator import itemgetter

jogos={'Jogador1':randint(1,6),
       'Jogador2':randint(1,6),
       'Jogador3':randint(1,6),
       'Jogador4':randint(1,6)}
rank=list()
print("Valores Sorteados!")
for k,v in jogos.items():
    print(f"{k} Tirou {v} no dado.")
    sleep(0.75)

rank=sorted(jogos.items(), key=itemgetter(1), reverse=True)

print("=-="*5,"RANKING","=-="*5)
for i,v in enumerate(rank):
    print(f"{i+1} Lugar {v[0]} com {v[1]}.")





