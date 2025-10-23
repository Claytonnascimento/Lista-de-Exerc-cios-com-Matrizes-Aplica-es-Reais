chuva = [
    [5, 10, 0, 2, 3, 8, 6],   
    [0, 0, 5, 3, 2, 1, 0],    
    [8, 12, 7, 5, 6, 10, 9]   
]

totais = [sum(chuva[i]) for i in range(3)]

for i, total in enumerate(totais):
    print(f"Cidade {i+1}: Total de chuva = {total} mm")

cidade_mais_chuva = totais.index(max(totais)) + 1
print(f"\nCidade com mais chuva na semana: Cidade {cidade_mais_chuva}")
