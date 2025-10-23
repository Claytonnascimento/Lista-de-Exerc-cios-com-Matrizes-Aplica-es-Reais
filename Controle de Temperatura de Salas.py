temperaturas = [
    [22.5, 23.0, 21.8],
    [24.0, 25.2, 24.5],
    [20.5, 21.0, 20.8],
    [23.3, 22.9, 23.5],
    [25.0, 24.8, 25.3]
]

medias = []
for sala in temperaturas:
    media = sum(sala) / len(sala)
    medias.append(media)

for i, media in enumerate(medias, start=1):
    print(f"Sala {i}: média = {media:.2f} °C")
