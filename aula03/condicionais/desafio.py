# Crie um programa que calcule o valor do frete com base na distância:
# Até 5km, R$5
# De 6km até 10Km, R$10
# Acima de 10km, exibir que a entrega não é feita.
# distancia = 3 # Altere este valor para testar

# if distancia <= 5:
#     print("O valor do frete é de R$5.")
# elif distancia <=10:
#     print("O valor do frete é de R$10.")
# else:
#     print("Infelizmente, não entregamos nessa distância.")

# Agora, a nossa pizzaria está cobrando uma `taxa fixa de R$5 por entrega`, além de `R$1 por km até 5km,
# ` e `R$2 por km até 10km`. Mais ainda `não entregamos com a distância superior a 10km`.

# Pegando como base essas possibilidades, faça um programa que responda as seguintes perguntas:

# - Quanto Joana irá pagar de frete, sendo que mora a 8km da pizzaria.
# - Quanto Guilherme irá pagar de frete, sendo que mora a 3km da pizzaria.
# - Quanto Rafael irá pagar de frete, sendo que mora a 11km da pizzaria.

distancia = int(input("Insira a distância:"))

if distancia <= 5:
    frete = 5 + distancia
    print("A taxa de entrega é de",frete,"reais.")
elif distancia <= 10:
    frete = 5 + 2*distancia
    print("A taxa de entrega é de",frete,"reais.")
else:
    print("Não entrega.")