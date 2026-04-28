alunos = int(input("Informe a quantidade de alunos: "))
notas = []
for i in range(alunos):

    while True:
        nota = int(input(f"Digite a nota do aluno {i+1}: "))
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        else:
            print("Nota inválida. Digite uma nota entre 0 e 10.")

abaixo_media = sum(1 for n in notas if n < 6)
na_media = sum(1 for n in notas if n >= 6)

print("Alunos abaixo da média:", abaixo_media)
print("Alunos na média:", na_media)

