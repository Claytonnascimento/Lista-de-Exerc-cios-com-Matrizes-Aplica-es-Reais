notas = [
    [7.5, 8.0, 6.5],
    [9.0, 8.5, 9.5],
    [6.0, 7.0, 6.5],
    [8.0, 7.5, 8.0]
]

medias_alunos = [sum(aluno)/len(aluno) for aluno in notas]

medias_provas = [sum(notas[i][j] for i in range(4)) / 4 for j in range(3)]

print("Médias por aluno:")
for i, media in enumerate(medias_alunos, start=1):
    print(f"Aluno {i}: {media:.2f}")

print("\nMédias por prova:")
for j, media in enumerate(medias_provas, start=1):
    print(f"Prova {j}: {media:.2f}")
