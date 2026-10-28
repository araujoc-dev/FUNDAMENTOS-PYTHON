r1=float(input("1* Segmento: "))
r2=float(input("2* Segmento: "))
r3=float(input("3* Segmento: "))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print(f"Os segmentos {r1}, {r2}, {r3} Podem formar um triangulo!")
else:
    print(f"Os segmentos {r1}, {r2}, {r3} NÃO Podem formar um triangulo!")