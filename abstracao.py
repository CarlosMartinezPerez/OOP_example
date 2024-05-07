from abc import ABC, abstractmethod


class Pessoa(ABC):  # Classe abstrata Pessoa
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def apresentar(self):  # Método abstrato
        pass


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):  # Implementação do método abstrato apresentar
        print(f"Olá! Sou o aluno {self.nome}, tenho {self.idade} anos e minha matrícula é {self.matricula}.")


class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def apresentar(self):  # Implementação do método abstrato apresentar
        print(f"Olá! Sou o professor {self.nome}, tenho {self.idade} anos e leciono a disciplina de {self.disciplina}.")


# Exemplo de uso das classes
aluno1 = Aluno("Maria", 25, "2021001")
aluno1.apresentar()

professor1 = Professor("Carlos", 35, "Matemática")
professor1.apresentar()

'''
Neste exemplo, a classe Pessoa é uma classe abstrata que contém um método abstrato apresentar(). 
Essa classe serve como um modelo genérico para pessoas na administração escolar, mas não pode ser instanciada diretamente.
As subclasses Aluno e Professor estendem a classe Pessoa e implementam o método abstrato apresentar() de 
forma específica para cada tipo de pessoa.
A abstração permite definir um modelo genérico para pessoas na escola, mas a implementação dos detalhes específicos é 
deixada para as subclasses. Isso promove uma estrutura de código mais flexível e escalável.
'''