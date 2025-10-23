horarios = [
    ["06:30", "12:00", "18:15"],  
    ["07:00", "13:30", "19:00"],  
    ["06:45", "12:15", "17:45"],  
    ["07:15", "13:00", "18:30"]   
]

print(" Linhas disponíveis:")
for i in range(1, 5):
    print(f"Linha {i}")

linha = int(input("\nDigite o número da linha que deseja consultar (1 a 4): "))

if 1 <= linha <= 4:
    print(f"\n Horários da Linha {linha}:")
    for i, hora in enumerate(horarios[linha - 1], start=1):
        print(f"Horário {i}: {hora}")
else:
    print(" Linha inválida! Digite um número entre 1 e 4.")
