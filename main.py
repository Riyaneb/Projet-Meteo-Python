class relevéMétéo:
    def __init__(self,liste):
        self.ville = liste[0]
        self.temperature = float(liste[1])
        self.humidite = float(liste[2])

    def Canicule(self):
        if self.temperature > 25.0:
            return True
        else:
            return False



with open("data.csv","r") as f:
    next(f)
    for ligne in f:
        lignePropre= ligne.strip()
        liste = lignePropre.split(",")
        Releve = relevéMétéo(liste)
        if Releve.Canicule():
            print(f"Attention, canicule à {Releve.ville}")


