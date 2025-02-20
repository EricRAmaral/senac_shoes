"""
### **Caixa Eletrônico 💰**

💡 **Enunciado**:

Crie um programa que simule um caixa eletrônico. O usuário deve poder sacar valores até que o saldo disponível acabe ou até que ele digite "sair".

📝 **Regras:**

- Comece com um saldo inicial de R$ 500.
- Peça para o usuário digitar um valor para saque.
- Se o valor for maior que o saldo, avise que não há saldo suficiente.
- Se o usuário digitar "sair", encerre o programa.
"""

saldo = 500 # Valor referente ao saldo inicial do usuário.

while saldo > 0: # O laço while continuará sendo executado até que saldo acabe(False).
    print(f' \n Saldo disponível: R$ {saldo:.2f}') # \n realiza quebra de linha.
    saque = input("Digite o valor ara sacar ou 'sair' para encerrar: ")
    
    if saque.lower() == "sair": # lower transforma a string em minúscula.
        print("Operação encerrada.")
        break

    saque = float(saque)
    if saque > saldo:
        print("Saldo insuficiente.")
    else:
        # saldo = saldo - saque # redeclaração de variável
        saldo -= saque # operação de decremento
        print(f"Saque de R$ {saque:.2f} realizado!")