# classes Pessoa, Professor, Aluno

# criando a superclass pessoa
class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    def exibir_dados(self):
        return f'Nome: {self.nome} | Idade: {self.idade} | CPF: {self.cpf}'
    
# criando a subclass aluno
class Aluno(Pessoa):
    def __init__(self, nome, idade, cpf, matricula):
        super().__init__(nome, idade, cpf)
        self.matricula = matricula
        self.notas = [] # Lista para armazenar notas do aluno
    def adicionar_notas(self, nota):
        self.notas.append(nota)
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    def exibir_dados(self):
        return f'{super().exibir_dados()} | Matricula: {self.matricula}'
    
# criando a subclass professor
class Professor(Pessoa):
    def __init__(self, nome, idade, cpf, disciplina, salario):
        super().__init__(nome, idade, cpf)
        self.disciplina = disciplina
        self.salario = salario
    def exibir_dados(self):
        return f'{super().exibir_dados()} | Disciplina: {self.disciplina} | Salário: {self.salario:.2f}'
    
# criando alunos e professores

aluno1 = Aluno("Maria Souza", 16, "123456", "2025001")
professor1 = Professor("Carlos Leiria", 48, "654321", "Matemática", 50000)

# exibindo
print(aluno1.exibir_dados())
print(professor1.exibir_dados())
