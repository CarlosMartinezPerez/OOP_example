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

    def estudar(self):
        print(f"{self.nome} está estudando.")

    def apresentar(self):  # Sobrescrevendo o método apresentar da classe Pessoa
        print(f"Olá! Sou o aluno {self.nome}, tenho {self.idade} anos e minha matrícula é {self.matricula}.")


# Exemplo de uso das classes
pessoa1 = Pessoa("João", 30)
pessoa1.apresentar()

aluno1 = Aluno("Maria", 25, "2021001")
aluno1.apresentar()
aluno1.estudar()


'''
Neste exemplo, a classe Pessoa é a classe base, que possui atributos comuns a todas as pessoas, como nome e idade, 
e um método apresentar() que imprime uma mensagem de apresentação.
A classe Aluno é uma classe derivada que herda da classe Pessoa. Ela adiciona um atributo adicional matricula 
e um método estudar(). Além disso, ela sobrescreve o método apresentar() para incluir informações específicas 
do aluno, como a matrícula.
Quando criamos uma instância da classe Aluno, ela herda automaticamente todos os atributos e métodos da classe Pessoa, 
além de ter acesso aos atributos e métodos próprios da classe Aluno. Isso demonstra o conceito de herança em Python.
1'''
