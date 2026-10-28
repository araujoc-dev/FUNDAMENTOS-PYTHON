from random import randint
v=0
print(f"{"=-="*10}\nJOGO DO PAR OU IMPAR\n{"=-="*10}")
while True:
    jg=int(input("Diga um valor: "))
    pc=randint(0,10)
    partida=jg+pc
    tipo=" "
    while tipo not in "PI":
        tipo=str(input("Par ou Impar? [P/I]: ")).strip().upper()[0]
    print(f"{"="*30}\nVocê jogou [{jg}] e PC [{pc}]. Total: {partida}")
    print(f"DEU PAR" if partida % 2 ==0 else "DEU IMPAR")
    if tipo == "P":
        if partida % 2 == 0:
            print("Venceu!")
            v+=1
        else:
            print("Derrota!")
            break
    elif tipo == "I":
        if partida % 2 == 1:
            print("Venceu!")
            v+=1
        else:
            print("Derrota!")
            break
    print("Jogar novamente!")
print(f"Voce ganhou {v} vezes.")