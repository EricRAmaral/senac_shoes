# SINTAXE BÁSICA DE UMA FUNÇÃO

def nome_da_funcao(parametros):
    #codigo da funcao
    resultado = 0
    return resultado

# Função sem retorno
def ola_mundo():
    print("Olá mundo.")

ola_mundo() # chamando a função, invocando a função

# Função com parâmetros

def saudacao(nome):
    print(f"Olá, seja bem-vendo(a) {nome}")

saudacao("Eric")
saudacao("Laila")

# Função com parâmetro e retorno
def somar(numero1, numero2):
    soma = numero1 + numero2
    return soma

print(somar(1,2))