from collections import Counter
import math, random 



# Gemiddelde berekenen
def aantal(getallen):
        return len(getallen)
    #  len(getallen)


# Som van alle getallen in de lijst
def som (getallen):
    return sum(getallen)

# Gemiddelde berekenen
def gemiddelde(getallen):
    return sum(getallen) / aantal(getallen)
    


# Het grootste getal in de lijst
def grootste_getal(getallen):
    return max(getallen)


# Het kleinste getal in de lijst

def kleinste_getal(getallen):
    return min(getallen)

# Het eerste getal in de lijst
def eerste_getal(getallen):
    return getallen[0]
    

# Het kleinste getal gedeeld door het eerste controle getal
def delen1(getallen,controlegetal1):
    return kleinste_getal(getallen) / controlegetal1


# Het grootste getal gedeeld door het tweede controle getal
def delen2(getallen,controlegetal2):
    return grootste_getal(getallen) / controlegetal2


# alle unieke getallen
def unieke_getallen(getallen:list)->list:
    return list(set(getallen))

# Aantal unieke elementen in de lijst
def aantal_unieke_elementen(getallen:list)->int:
    return len(unieke_getallen(getallen))


# Verschil tussen aantal unieke elementen en eerste controle getal
def verschil1(getallen,controlegetal1):
    return aantal_unieke_elementen(getallen) - controlegetal1

# Sorteer de lijst van getallen
def gesorteerde_lijst(getallen):
    return sorted(getallen)

# Sorteer de lijst van unieke getallen
def gesorteerde_lijst_uniek(getallen):
    return sorted(unieke_getallen(getallen))

# Tel het aantal keren dat elk uniek element voorkomt in de lijst

# def telling_elementen(getallen):
#     return Counter(getallen)
def telling_elementen(getallen):
    telling_elementen = {}
    for getal in getallen:
        aantalkeer = telling_elementen[getal]+1 if getal in telling_elementen else 1
        telling_elementen[getal] = aantalkeer
    return telling_elementen

# Getallen die deelbaar zijn door het eerste controlle getal
def deelbaar1(getallen,controlegetal1):
    deelbaar1 = []
    for getal in unieke_getallen(getallen):
        if getal % controlegetal1 == 0:
            deelbaar1.append(getal)
    deelbaar1 = sorted(deelbaar1)
    return deelbaar1



# Getallen die deelbaar zijn door het tweede controlle getal
def deelbaar2(getallen,controlegetal2):
    deelbaar2 = []
    for getal in unieke_getallen(getallen):
        if getal % controlegetal2 == 0:
            deelbaar2.append(getal)
    deelbaar2 = sorted(deelbaar2)
    return deelbaar2

# Controleer of een bepaald getallen in de lijst voorkomen
def komtvoor(getallen,controlegetal1,controlegetal2):
    return controlegetal1 in getallen and controlegetal2 in getallen
# komtvoor = controlegetal1 in getallen and controlegetal2 in getallen

# Vindt de posities van heteerste controle getal
def posities(getallen,controlegetal1):
    posities = []
    for index, num in enumerate(getallen):
        if num == controlegetal1:
            posities.append(index)
    return posities

# Standaardafwijking berekenen


def standaard_afwijking(getallen):
    gem = gemiddelde(getallen)
    aantal_elementen = aantal(getallen)
    
    verschil_kwadraat = sum((x - gem) ** 2 for x in getallen)
    variantie = verschil_kwadraat / aantal_elementen
    standaardafwijking = math.sqrt(variantie)
    return standaardafwijking


# Shuffle de lijst
def shuffled_list(getallen):
    geschudde_lijst = getallen.copy()
    random.shuffle(geschudde_lijst)
    return geschudde_lijst
    

# Pak een random getal uit de lijst
def random_getal(getallen):
    return random.choice(getallen)if getallen else None


# Verschil tussen twee getallen
def verschil2(wilkeurige_getaal,controlegetal2,):
    return wilkeurige_getaal - controlegetal2


def analyseer_getallenlijst(getallen, controle_getal1, controle_getal2):
    if not getallen:
        return {"Fout": "Lijst is leeg. Voer getallen in."}

    if not isinstance(controle_getal1, int) or not isinstance(controle_getal2, int):
        return {"Fout": "Controlegetallen moeten gehele getallen zijn."}
    wilkeurige_getaal= random_getal(getallen)
    resultaten = {
        "Aantal Getallen": aantal(getallen),
        "Gemiddelde": gemiddelde(getallen),
        "Som": som(getallen),
        "Maximum Element": grootste_getal(getallen),
        "Minimum Element": kleinste_getal(getallen),
        "Eerste Element": eerste_getal(getallen),
        f"{kleinste_getal(getallen)} / {controle_getal1}": delen1(getallen, controle_getal1),
        f"{grootste_getal(getallen)} / {controle_getal2}": delen2(getallen, controle_getal2),
        "Aantal Unieke Elementen": aantal_unieke_elementen(getallen),
        f"Verschil tussen {aantal_unieke_elementen(getallen)} & {controle_getal1}": verschil1(getallen, controle_getal1),
        "Gesorteerde Lijst van Getallen": gesorteerde_lijst(getallen),
        "Gesorteerde Lijst van Unieke Elementen": gesorteerde_lijst_uniek(getallen),
        "Telling van elementen": telling_elementen(getallen),
        f"Deelbaar door {controle_getal1} (op volgorde)": deelbaar1(getallen, controle_getal1),
        f"Deelbaar door {controle_getal2} (op volgorde)": deelbaar2(getallen, controle_getal2),
        f"Bevat {controle_getal1} & {controle_getal2}": komtvoor(getallen, controle_getal1, controle_getal2),
        f"Posities van {controle_getal1}": posities(getallen, controle_getal1),
        "Standaard Afwijking": standaard_afwijking(getallen),
        "Geschudde Lijst": shuffled_list(getallen),
        "Willekeurig Getal": wilkeurige_getaal,
        f"Het verschil tussen {wilkeurige_getaal} & {controlegetal2}": verschil2(wilkeurige_getaal, controle_getal2),
        
    }

    return resultaten


# Voorbeeld van het gebruik van de functie:
getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
controlegetal1 = 8
controlegetal2 = 3
analyse_resultaat = analyseer_getallenlijst(getallenlijst, controlegetal1, controlegetal2)
print("Analyse resultaten:")
for key, value in analyse_resultaat.items():
    print(f"{key}: {value}")


