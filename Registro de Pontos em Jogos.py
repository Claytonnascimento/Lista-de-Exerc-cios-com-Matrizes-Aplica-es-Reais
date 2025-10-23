pontos = [
    [3, 1, 0, 3],  
    [2, 2, 3, 1], 
    [1, 3, 3, 2]   
]

totais = [sum(time) for time in pontos]

maior_pontuacao = max(totais)
time_vencedor = totais.index(maior_pontuacao) + 1

print("🏆 Pontuação Total por Time:\n")
for i, total in enumerate(totais, start=1):
    print(f"Time {i}: {total} pontos")

print(f"\n🥇 O time com maior pontuação é o **Time {time_vencedor}**, com {maior_pontuacao} pontos!")
