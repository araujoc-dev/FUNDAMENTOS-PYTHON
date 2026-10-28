soma=cont=0
while True:
    n=int(input("[0] Para parar. Digite um valor: "))
    if n == 0:
        break
    cont+=1
    soma+=n
print(f"A soma dos {cont} numeros foi: {soma}")