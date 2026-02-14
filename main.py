with open("data.csv","r") as f:
    next(f)
    for ligne in f:
        lignePropre= ligne.strip()
        liste = lignePropre.split(",")
        if int(liste[1]) > 25:
            print(f"Attention, canicule dans la ville de {liste[0]} avec une temperature de {liste[1]}C° et une humidité de {liste[2]}")
