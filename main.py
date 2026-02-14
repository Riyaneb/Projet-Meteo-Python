import requests
import reverse_geocoder as rg
import sqlite3

class relevéMétéo:
    def __init__(self,liste):
        coord = (float(liste[1]),float(liste[0]))
        self.ville = rg.search([coord])
        self.temperature = float(liste[3])

    def Canicule(self):
        if self.temperature > 25.0:
            return True
        else:
            return False
        
    def Gele(self):
        if self.temperature < 5:
            return True
        else:
            return False
        
def moyenne(liste):
    cpt=0
    n=0
    for i in liste:
        cpt += float(i)
        n += 1
    return cpt/n

        
API = "https://api.open-meteo.com/v1/forecast?latitude=48.8534,45.7485,43.297,44.8404,48.85,48.112,50.633,43.7031,43.6043,48.5839,47.2172&longitude=2.3488,4.8467,5.3811,-0.5805,2.6,-1.6743,3.0586,7.2661,1.4437,7.7455,-1.5534&hourly=temperature_2m&timezone=auto"
r = requests.get(API)

if r.status_code == 200:
    donnee = r.json()
    if donnee == None:
        print("Donnée JSON non récupéré")
    else:
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Meteo
                (Longitude real, Latitude real, Elevation real, Temperature real)''')
        c.execute('''DELETE FROM Meteo''')
        for ville in donnee:
            liste = ville['hourly']['temperature_2m']
            temp = moyenne(liste)
            tmp = ('''INSERT INTO Meteo VALUES (?,?,?,?)''')
            champ = (ville['longitude'],ville['latitude'],ville['elevation'],temp)
            c.execute(tmp,champ)
        conn.commit()

        nb = 0

        for i in c.execute('SELECT * FROM Meteo'):
            Releve = relevéMétéo(i)
            if Releve.Canicule():
                print(f"Attention, canicule à {Releve.ville[0]['name']} : {Releve.temperature:.2f}C°")
                nb += 1
            elif Releve.Gele():
                print(f"Attention, Ca gèle à {Releve.ville[0]['name']} : {Releve.temperature:.2f}C°")
                nb += 1
        if nb == 0:
            print("Problème nulle part")
 

        
        conn.close()
else:
    print("Probème avec l'api")



