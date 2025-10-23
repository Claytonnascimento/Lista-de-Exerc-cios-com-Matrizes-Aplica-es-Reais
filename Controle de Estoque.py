estoques = [
    [10, 12, 8],   
    [5, 7, 9],     
    [20, 18, 22], 
    [15, 10, 12]   
]

totais = [sum(produto) for produto in estoques]

print("Estoque Total por Produto:\n")
for i, total in enumerate(totais, start=1):
    print(f"Produto {i}: {total} unidades")
