repeticoes = [
    [15, 20, 25],
    [10, 15, 20],
    [12, 18, 22],
    [14, 16, 24]
]

for j in range(3):
    total = sum(repeticoes[i][j] for i in range(4))
    print(f"Exercício {j+1}: Total de repetições = {total}")
