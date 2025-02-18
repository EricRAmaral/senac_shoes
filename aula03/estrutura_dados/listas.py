"""
Homogêneo -> Aceita apenas um único tipo de dado
Heterogêneo -> Aceita dados de tipos diferentes
"""

# Declaração Listas
# Ordenadas, mutáveis e heterogêneas

sabores = ["mussarela","calabresa","frango com catupiry","poruguesa"]
dados_pizza = ["mussarela", 26.90, True]
print("Sabores disponíveis: ", sabores)
print("Informalçoes da pizza: ", dados_pizza)

# Operações com Listas
# 1. append() -> Adicionar um novo valor ao final da lista
sabores.append("margherita")
print("Sabores disponíveis: ",sabores)

# 2. remove() -> Remove um elemento da lista.
sabores.remove("calabresa")
print("Sabores disponíveis: ",sabores)

# 3. Acessando os elementos.
pizzas = ["mussarela", "calabresa", "frango com catupiry", "portuguesa"]
print(pizzas[0])
print(pizzas[-1])