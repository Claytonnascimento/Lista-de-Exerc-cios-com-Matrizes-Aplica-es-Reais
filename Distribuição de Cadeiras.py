sala = [
    ["O", "X", "O", "O", "X", "O"],
    ["X", "O", "O", "X", "O", "O"],
    ["O", "O", "X", "O", "O", "X"],
    ["X", "X", "O", "O", "O", "O"],
    ["O", "O", "O", "X", "O", "X"]
]

print("Mapa das cadeiras (X = ocupada, O = livre):\n")
for fila in sala:
    print(" ".join(fila))
