from datetime import datetime
cadunico=dict()
cadunico['nome']=str(input("Nome: "))
nasc=int(input("Ano de Nascimento: "))
cadunico['idade']= datetime.now().year - nasc
cadunico['carteirat']=int(input("Carteira de Trabalho [0] CASO NÃO TENHA : "))
if cadunico['carteirat'] != 0:
    cadunico['contrata']=int(input("Ano de Contratação: "))
    cadunico['salario']=float(input("Salário: R$ "))
    cadunico['aposentar']= (cadunico['contrata'] + 35) - datetime.now().year

print('=-='*30)
for k,v in cadunico.items():
    print(f"{k} Tem o Valor {v}.")
