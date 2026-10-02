from aluno import Aluno
from disciplina import Disciplina

# criar / instanciar um aluno
aluno1 = Aluno("Joauquim", "3546213", "Ciência da Computação")

# print(aluno1.disciplinas)
#: []

# criar / instanciar 2 disciplinas
sers = Disciplina("Soluções Renováveis", "Triatiack")
model_mat = Disciplina("Modelagem Matemática", "Roberto")

# matricular o aluno nas 2 disciplinas

aluno1.matricular(sers)
aluno1.matricular(model_mat)

# print(aluno1.disciplinas[0].professor)
#: Triatiack

aluno1.add_nota(sers, 7.5)

# print(aluno1.notas_por_disciplina)
#: {'Soluções Renováveis': [7.5], 'Modelagem Matemática': []}

aluno1.add_nota(sers, 3.5)
aluno1.add_nota(model_mat, 4.5)
aluno1.add_nota(model_mat, 7)

# print(aluno1.notas_por_disciplina)
#: {'Soluções Renováveis': [7.5, 3.5], 'Modelagem Matemática': [4.5, 7]}

print(aluno1.calc_media_disciplina(sers))