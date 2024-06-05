def is_even(number: int) -> bool:
    return number % 2 == 0

# deze functie neemt de parameter als een invoer en rtuneert een boeling (True ale het even is en False ales eht oneven is )

resultaat = is_even(int(input('geef en getaal: ')))
print(resultaat)

def revers_woords(string:str) -> str:
    worden = string.split()
    reverd_woords = worden[::-1]
    reversd_string = ' '.join(reverd_woords)
    return reversd_string

# deze functie draait de string worden achterste voren

print(revers_woords("yousef alkurdi is 23 jaar oud.")) 

def unique_chars_counter(sentence:str) -> int:
    unique_chars = set(sentence)
    character_counter = len(unique_chars)
    return character_counter

# Deze functie telt de aantal unieke karakters in de string en geeft de aantal terug (Uneke karakters zijn die letters die niet meer herhaald worden)       
                   
resultaat = unique_chars_counter('hello world')
print("Het aantal unieke karakters is:", resultaat)  

def gemiddelde_woordlengte(zin: str) -> float:
    woorden = zin.split()
    
    totale_lengte = 0
    for woord in woorden:
        totale_lengte += len(woord)

    gemiddelde_woordlengte = totale_lengte / len(woorden)
    return gemiddelde_woordlengte

# deze functie verandert een string in een list en telt de characters van elke item in de list en telt ze op en daarna deelt ze door de aantal items in de list

print(gemiddelde_woordlengte("hallo.yousef yousef"))

def print_tafels(getal: int, aantal_keer: int = 10) -> None:
    for teller in range(1, aantal_keer + 1):
        product = teller * getal
        print(f'{teller} x {getal} = {product}')

# De functie spaghetti_spaceship genereert en drukt een tafel van vermenigvuldiging af voor een specifiek getal (infinity_pizza). Deze tafel wordt een aantal keer afgedrukt dat wordt bepaald door het argument parallelle_tosti
#in het gevaal dat je de aantal vermenigvuldiging is niet aan ge geven word de aan gegeven getaal vermenigvuldigt met 10

print_tafels(5,5)






