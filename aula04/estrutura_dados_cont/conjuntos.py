"""
Os conjuntos não são ordenadoas, são mutáveis, heterogêneos ou homogêneos
e não permitem elementos duplicados.
"""

# Declaração dos conjuntos 
ingredientes = {"mussarela", "calabresa", "tomate", "azeitona", "tomate"}
print("Ingredientes básicos: ", ingredientes)

# Operação com os conjuntos
# Adicionar itens:
ingredientes.add("oregano")
print("Ingredientes atualizados: ", ingredientes)

# Remover itens:
ingredientes.remove("azeitona")
print("Ingredientes atualizados: ", ingredientes)

# União de conjuntos:
adicionais = {"bacon", "palmito"}
todos_ingredientes = ingredientes.union(adicionais)
print("Todos os ingredientes: ",todos_ingredientes)

# Interseção de conjuntos:
pizza_vegana = {"tomate", "azeitona", "rucula"}
comuns = ingredientes.intersection(pizza_vegana)
print("Ingredientes em comum: ", comuns)