# 2. **Verificação de Ingredientes**
    
#     Dado dois conjuntos de ingredientes, `exiba os ingredientes comuns entre eles` e os `que estão disponíveis apenas em um conjunto.`

ingredientes = {"mussarela", "pepperoni", "catupiry", "milho"}
ingredientes2 = {"mussarela", "frango", "cebola", "catupiry"}

comum = ingredientes.intersection(ingredientes2)
print(comum)

exclusivos = ingredientes.difference(ingredientes2)
print(exclusivos)
