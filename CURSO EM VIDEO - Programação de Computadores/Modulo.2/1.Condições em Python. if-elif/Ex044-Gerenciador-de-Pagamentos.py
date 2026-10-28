compra=float(input("Preço das compras: R$"))
print("FORMAS DE PAGAMENTO!\n[1] À Vista Dinheiro/Cheque.\n[2] À Vista Cartão.\n[3] 2x Cartão.\n[4] 3x ou Mais no Cartão.")
opcao=int(input("Qual forma de pagamento?: "))
if opcao == 1:
    print(f"Sua compra de {compra:.2f} vai custar {compra-(compra*0.1):.2f} no final.")
elif opcao == 2:
    print(f"Sua compra de {compra:.2f} vai custar {compra-(compra*0.05):.2f} no final.")
elif opcao == 3:
    parcela = 2
    print(f"Sua compra vai custar {compra:.2f}.")
    print(f"Sua compra será parcelada em {parcela}x de {compra/parcela:.2f}")
elif opcao == 4:
    parcela = int(input("Quantas parcelas?: "))
    print(f"Sua compra será parcelada em {parcela}x de {(compra+(compra*0.2))/parcela:.2f}")
    print(f"Sua compra de {compra} vai custar {compra+(compra*0.2):.2f} no final.")