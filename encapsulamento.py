class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo público
        self.idade = idade  # Atributo público
        self.__matricula = None  # Atributo privado iniciado como None

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def estudar(self):
        print(f"{self.nome} está estudando.")

    def apresentar(self):
        print(f"Olá! Sou o aluno {self.nome}, tenho {self.idade} anos e minha matrícula é {self.__matricula}.")


# Exemplo de uso da classe Aluno
aluno1 = Aluno("Maria", 25)
aluno1.apresentar()

# Tentando acessar diretamente o atributo privado
# Isso causará um erro, pois o atributo __matricula é privado
# print(aluno1.__matricula)

# Acessando o atributo privado por meio de métodos get e set
aluno1.set_matricula("2021001")
print("Matrícula:", aluno1.get_matricula())
aluno1.apresentar()

'''
Neste exemplo, a classe Aluno possui um atributo público nome e um atributo privado __matricula. 
Usamos o prefixo de duplo sublinhado __ para tornar o atributo __matricula privado.
Para acessar e modificar o atributo privado __matricula, definimos métodos get_matricula() e set_matricula(matricula) 
que permitem obter e definir o valor da matrícula de forma controlada.
Dessa forma, o encapsulamento permite controlar o acesso aos atributos da classe, garantindo que eles sejam acessados e 
modificados apenas por meio de métodos específicos, o que aumenta a segurança e a robustez do código.
'''
