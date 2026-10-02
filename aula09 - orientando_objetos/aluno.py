from disciplina import Disciplina

class Aluno:
    def __init__(self, nome, rm, curso):
        self.nome = nome
        self.rm = rm
        self.curso = curso
        self.disciplinas = []               # [Disciplina, Diciplina, ...]
        self.notas_por_disciplina = {}      # {"Nome disciplina": [nota1, nota2,...], ...}

    def matricular (self, disciplina: Disciplina): # tipagem :Disciplina, é tipo dizer que é uma string, mas com outro tipo de dado
        self.disciplinas.append(disciplina)
        self.notas_por_disciplina.setdefault(disciplina.nome, []) # seta um valor inicial

    def add_nota(self, disciplina: Disciplina, nota: float):
        self.notas_por_disciplina [disciplina.nome].append(nota)

    def calc_media_disciplina (self, d: Disciplina) -> float: # d = disciplina # -> float OUTPUT = float
        notas = self.notas_por_disciplina.get(d.nome, []) # defalt = [] = quando não achar nada
        if notas: return sum(notas)/len(notas)
        else: return 0