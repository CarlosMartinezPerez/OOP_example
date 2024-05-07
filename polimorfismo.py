class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome} e tenho {self.idade} anos.")


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        print(f"Olá! Sou o aluno {self.nome}, tenho {self.idade} anos e minha matrícula é {self.matricula}.")


class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def apresentar(self):
        print(f"Olá! Sou o professor {self.nome}, tenho {self.idade} anos e leciono a disciplina de {self.disciplina}.")


# Exemplo de uso das classes
pessoa1 = Pessoa("João", 30)
pessoa1.apresentar()

aluno1 = Aluno("Maria", 25, "2021001")
aluno1.apresentar()

professor1 = Professor("Carlos", 35, "Matemática")
professor1.apresentar()

'''
Neste exemplo, a classe Pessoa é a classe base, que possui um método apresentar() com uma implementação genérica.
As classes Aluno e Professor são subclasses de Pessoa e têm seus próprios métodos apresentar(), que são polimórficos. 
Cada uma dessas subclasses implementa o método apresentar() de forma diferente para fornecer informações específicas 
sobre alunos e professores.
Quando chamamos o método apresentar() para cada instância de Pessoa, o método apropriado é executado com base no tipo da 
instância, demonstrando assim o polimorfismo em ação.
'''