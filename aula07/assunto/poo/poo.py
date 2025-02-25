# aluno -> nome, idade, endereço, cpf
class Aluno: #PascalCase para classes
    
    def __init__(self, nome, idade, endereco, cpf):
        self.nome = nome # Ana
        self.idade = idade # 22
        self.endereco = endereco # Rua 1
        self.cpf = cpf # 123
        self.matriculado = True # default, toda cópia da classe aluno vai ter essa característica

    # método que altera o status da matrícula do aluno
    def situacao(self):
        if self.matriculado == True:
            self.matriculado = False
        elif self.matriculado == False:
            self.matriculado = True

    # método que exibe as informações do aluno
    def exibir_info(self):
        print(f'''
            DADOS DO ESTUDANTE
        O nome do(a) aluno(a) é {self.nome},
        e o CPF é {self.cpf}.        
        ''')

# Criando cópias da classe aluno (instânciação)
a1 = Aluno("Ana", 22, "Rua 1", "123456789")
a2 = Aluno("Bia", 20, "Rua 16", "987654321")

print(a1)
a1.exibir_info()