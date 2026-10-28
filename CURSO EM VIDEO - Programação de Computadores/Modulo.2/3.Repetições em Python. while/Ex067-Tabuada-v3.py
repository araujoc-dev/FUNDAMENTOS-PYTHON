while True:
    n=int(input("[Ver Tabuada] Numero: "))
    print("="*30)
    if n <0:
        break
    for c in range(1,11):
        print(f"{n} x {c} = {n*c}")
    print("="*30)
print(f"{("="*30)}\nEncerrando Tabuada.exe\n{("="*30)}")