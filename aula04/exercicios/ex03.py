# 3. **Atualizar Cardápio**
    
#     `Crie` um `dicionário para o cardápio` e `adicione um novo sabor com preço`. `Atualize` o preço de um sabor existente e `remova` um sabor do cardápio.

cardapio = {
    "mussarela": 25.90,
    "pepperoni": 27.90,
    "frango com catupiry": 29.90
}
print(cardapio)

cardapio["catuperoni"] = 29.90
cardapio["frango com catupiry"] = 31.90
cardapio.pop("mussarela")
# del cardapio["mussarela"]

print(cardapio)