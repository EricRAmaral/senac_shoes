# Exercício Bônus 💡​
# Simulação de Senha de Banco 🔐​
# 💡 Enunciado:
# Crie um sistema que peça para o usuário digitar uma senha para acessar sua conta bancária. Ele tem apenas 3 tentativas para acertar a senha correta. Se ele errar as 3 vezes, o sistema bloqueia a conta.
# 📝 Regras:
# A senha correta é "1234".
# O usuário tem até 3 tentativas para acertar.
# Se errar as 3 vezes, exiba "🚫 Conta bloqueada!".
# 🔍 Exemplo esperado:
# Digite sua senha: 1111
# ❌ Senha incorreta! Tentativas restantes: 2
# Digite sua senha: 2222
# ❌ Senha incorreta! Tentativas restantes: 1
# Digite sua senha: 3333
# 🚫 Conta bloqueada!

SENHA_CORRETA = "1234"
tentativas = 3

while tentativas > 0:
    senha = input('Digite sua senha: ')

    if senha == SENHA_CORRETA:
        print("Acesso permitido.")
        break
    else:
        tentativas -= 1
        print(f'Senha incorreta. Tentativas restanates: {tentativas}')

if tentativas == 0: 
    print("Conta bloqueada.")        