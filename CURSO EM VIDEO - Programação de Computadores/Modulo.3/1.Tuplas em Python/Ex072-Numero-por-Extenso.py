extenso=('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete','Oito', 'Nove', 'Dez')
dnv=''
while dnv in "S":
    num=int(input('Digite um número entre 0 e 10: '))
    if 0 <= num <=10:
        print(extenso[num]) 
