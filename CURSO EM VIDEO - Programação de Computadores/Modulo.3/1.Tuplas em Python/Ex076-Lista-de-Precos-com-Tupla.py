lista=('lapis', 1.75,'Borracha', 2,'Caderno',15.90,'Estojo',25,'Mochila', 120.32,'Canetas',22.30,'Livro',34.50)
print(f'{'-'*40}\n{'Lista de Preços':^40}\n{'-'*40}')
for i in range(0,len(lista)):
    if i %2==0:
        print(f'{lista[i]:.<30}',end='')
    else:
        print(f'R${lista[i]:>.2f}')