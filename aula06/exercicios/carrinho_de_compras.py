""" Carrinho de Compras 🛒​
💡 Enunciado:
Crie um programa que permita adicionar produtos a um carrinho de compras. O programa deve continuar pedindo produtos até que o usuário digite "finalizar". No final, exiba todos os produtos comprados.
📝 Regras:
O usuário digita o nome do produto e ele é adicionado a uma lista.
Se o usuário digitar "finalizar", o programa encerra e mostra os produtos comprados.
🔍 Exemplo esperado:
Digite um produto para adicionar ao carrinho (ou 'finalizar' para encerrar): Pizza
Produto 'Pizza' adicionado ao carrinho!
Digite um produto para adicionar ao carrinho (ou 'finalizar' para encerrar): Refrigerante
Produto 'Refrigerante' adicionado ao carrinho!
Digite um produto para adicionar ao carrinho (ou 'finalizar' para encerrar): finalizar

🛍️ Você comprou:
- Pizza
- Refrigerante """

# compras = []
# produto = ""

# while produto.lower() != 'finalizar':
#     compras.append(input("Digite um produto para adicionar ao carrinho (ou 'finalizar' para encerrar): "))
#     print("Você comprou:", compras)
#     if produto.lower() == 'finalizar':
#         break
# print("Compra finalizada:", compras)

carrinho = []
 
while True:
    produto = input("Digite um produto para adicionar no carrinho (ou 'finalizar' parar encerrrar): ")

    if produto.lower() == 'finalizar':
        print(" Fechando o carrinho.")
        break

    carrinho.append(produto)
    print(f"{produto} adicionado ao carrinho.")

if len(carrinho) > 0:
    print(" Você comprou: ")
    for item in carrinho:
        print(f"{item}")
else:
    print("Nenhum produto foi comprado.")



