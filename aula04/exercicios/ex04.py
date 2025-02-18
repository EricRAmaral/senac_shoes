# 4. **Controle de Estoque**
    
#     `Crie` um `dicionário com os estoques` de cada sabor. `Decremente` o estoque conforme os pedidos feitos e exiba uma `mensagem se o estoque acabar.`

estoque = {
    "mussarela": 100,
    "calabresa": 75,
    "frango com catupiry": 59,
}

pedido_cliente = 101

for quantidade in estoque:
    if pedido_cliente >= quantidade:
        print("Indisponível")






# for pedido_cliente in estoque:
#     if estoque[] < pedido_cliente
#         print 