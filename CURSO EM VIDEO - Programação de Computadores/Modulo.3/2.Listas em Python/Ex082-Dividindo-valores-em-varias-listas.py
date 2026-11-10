lista=[]
impares=[]
pares=[]
while True:
    n=int(input("Digite um valor: "))
    lista.append(n)
    if n % 2 ==0:
        pares.append(n)
    else:
        impares.append(n)
    resp=str(input("Deseja continuar? "))
    if resp in 'Nn':
        break
print(f"Lista completa: {lista}\nNumeros Pares: {pares}\nNumeros Impares: {impares}")
