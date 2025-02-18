# 1. **Lista de Pedidos**
    
#     `Crie uma lista de sabores de pizzas pedidos` pelo cliente. Adicione `3 sabores à lista` e `remova 1 sabor.` Exiba o pedido final.

sabores = ["mussarela", "calabresa", "portuguesa"]
# print(sabores)

sabores.append("bacon com ovos")
sabores.append("frango com catupiry")
sabores.append("pepperoni")
# print(sabores)

sabores.remove("bacon com ovos")
print(sabores)