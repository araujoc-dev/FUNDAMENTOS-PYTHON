print(f"{"=-="*10}\nLOJAS ARAUJO.DEV\n{"=-="*10}")
soma=maismil=maisbarato=cont=0
produtobarato=""
while True:
    produto=str(input("Produto: ")).title()
    preco=float(input("Preço: "))
    cont+=1
    soma+=preco
    if preco > 1000:
        maismil+=1
    if cont == 1:
        maisbarato = preco
    else:
        if preco < maisbarato:
            maisbarato = preco
            produtobarato = produto
    continua=" "
    while continua not in "SN":
        continua=str(input("Continuar? [S/N]: ")).upper().strip()[0]
    if continua == "N":
        break
print("~~ FIM DO PROGRAMA ~~")
print(f"Total da compra: {soma:.2f}\nProdutos +Mil: {maismil}\nProduto mais barato: {produtobarato} de {maisbarato:.2f}")