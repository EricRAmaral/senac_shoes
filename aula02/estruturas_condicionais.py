# # No Brasil, para alguém dirigir a pessoa precisa de 18 anos.
# Se a pessoa tiver a partir de 18 anos, pode dirigir.
# Se ela tiver entre 0 até 17 anos, não pode dirigir.
# Senão, informe uma idade válida.

# idade_pessoa = -12

# if idade_pessoa >= 18:
#     print("Pode dirigir")
# elif idade_pessoa >= 0 and idade_pessoa <= 17:
#     print("Não pode dirigir")
# else:
#     print("Idade inválida")

# Condicional aninhada

idade = 18
habilitacao = True

if idade >= 18:
    if habilitacao == True:
        print("Você pode dirigir")
    else:
        print("Você precisa de uma habilitação para dirigir")
else:
    print("Idade insuficiente para dirigir")

