class Disciplina:
    def __init__(self, nome, professor): # instancias
        self.nome = nome
# atributo (molde) = self.nome
# instancia (objeto) = professor
        self.professor = professor

    def exibir_infos (self):
        print(f"Disciplina: {self.nome} | Prof: {self.professor}")

# cs = Disciplina("Computer Science", "MAUMAU")
# print(cs)
# output: <__main__.Disciplina object at 0x0000019D003E7230>
# cs.exibir_infos()
# output: Disciplina: Computer Science | Prof: MAUMAU
