class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def categoria_idade(self):
        if self.idade < 12:
            return "Criança"
        elif self.idade < 18:
            return "Adolescente"
        else:
            return "Adulto"


# Exemplo de uso da classe Aluno
aluno1 = Aluno("Maria", 10)
print(f"{aluno1.nome} é uma {aluno1.categoria_idade}.")

aluno2 = Aluno("João", 16)
print(f"{aluno2.nome} é um {aluno2.categoria_idade}.")

aluno3 = Aluno("Ana", 25)
print(f"{aluno3.nome} é um {aluno3.categoria_idade}.")

'''
Neste exemplo, a classe Aluno possui um método categoria_idade decorado com @property. Esse método é usado 
como uma propriedade, permitindo que seja acessado como um atributo, sem a necessidade de chamar explicitamente 
um método.
A propriedade categoria_idade calcula automaticamente a categoria de idade do aluno com base em sua idade. 
Dependendo da idade do aluno, a propriedade retornará "Criança", "Adolescente" ou "Adulto".
Quando criamos instâncias da classe Aluno, podemos acessar a propriedade categoria_idade como se fosse um 
atributo normal, sem a necessidade de chamar um método específico para isso. Isso torna o código mais limpo e legível.
'''