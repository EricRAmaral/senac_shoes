sabores = ["mussarela", "calabresa", "pepperoni", "quatros queijos", "frango com catupiry"]
pedido = ""

print("Faça seu pedido (digite 'sair' para encerrar): ")
while pedido.lower() != 'sair':
    pedido = input("Escolha um sabor de lista do cardápio: ")
    if pedido in sabores:
        print(f"{pedido} adicionado ao seu Pedido.")
    elif pedido.lower() == 'sair':
        print("Pedido encerrado!")
    else:
        print("Sabor indisponível, escolha outro sabor.")