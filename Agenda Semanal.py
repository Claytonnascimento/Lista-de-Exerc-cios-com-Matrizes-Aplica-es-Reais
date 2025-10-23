agenda = [
    ["Ana", "Bruno", "Carla"],       
    ["Daniel", "Elisa", "Felipe"],    
    ["Gabriela", "Henrique", "Igor"],
    ["Júlia", "Karina", "Lucas"],     
    ["Mariana", "Natan", "Olivia"]    
]

dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

print("Agenda do Consultório\n")

for i in range(5):
    print(f"{dias[i]}-feira:")
    for j in range(3):
        print(f"  Horário {j+1}: {agenda[i][j]}")
    print()
