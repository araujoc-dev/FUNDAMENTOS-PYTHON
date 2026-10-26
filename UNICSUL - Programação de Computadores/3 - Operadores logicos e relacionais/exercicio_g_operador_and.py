#g) A > B e C > D
A = float(input('Digite um valor para A: '))
B = float(input('Digite um valor para B: '))
C = float(input('Digite um valor para C: '))
D = float(input('Digite um valor para D: '))
if A > B and C > D:
  print(f'{A} Maior que {B} e {C} Maior que {D}')
elif A > B and C < D:
  print(f'{A} Maior que {B} e {C} Não é maior que {D}')
elif A < B and C > D:
  print(f'{A} Não é maior que {B} e {C} Maior que {D}')
else:
  print(f'{A} Não é maior que  {B} e {C} Não é maior que  {D}')