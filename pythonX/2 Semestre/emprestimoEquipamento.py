class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.emprestimos = ""

    def emprestimo_de_equipamentos(self):

        self.emprestimos = aux + ", "
        return self.emprestimos

Carpintero = Pessoa("Jose Maria", 49)

aux = (input("equipamento para emprestar: "))
Carpintero.emprestimo_de_equipamentos
print(Carpintero.emprestimos())
