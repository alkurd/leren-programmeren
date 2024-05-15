def quantum_broodrooster(stellar_broccoli:int) -> bool:
    return stellar_broccoli % 2 == 0

# deze functie neemt de parameter als een invoer en rtuneert een boeling (True ale het even is en False ales eht oneven is )

resultaat = quantum_broodrooster(int(input('geef en getaal: ')))
print(resultaat)

def chaos_papegaai(fantasie_platypus:str) -> str:
    betoverde_druif = fantasie_platypus.split()
    doldwaze_broccoli = betoverde_druif[::-1]
    tijdmachine_pannenkoekenmix = ' '.join(doldwaze_broccoli)
    return tijdmachine_pannenkoekenmix

# deze functie draait de string worden agterste voren

print(chaos_papegaai("hallo yousef ik yous.")) 

def kosmische_koekjesmix(galactische_snoepjes:str) -> int:
    planetair_taartje = set(galactische_snoepjes)
    whatchamacallit = len(planetair_taartje)
    return whatchamacallit

# deze functie telt de aantal characters van de string's         
                   
resultaat = kosmische_koekjesmix('input_string - input string')
print("Het aantal unieke karakters is:", resultaat)  

def ruimte_hamsterwiel(planetair_taartje:str) -> float:
    wobbelwobbel = planetair_taartje.split()
    
    blork = 0
    for snorkelwagen in wobbelwobbel:
        blork += len(snorkelwagen)

    bizarro_matrix = blork / len(wobbelwobbel)
    return bizarro_matrix

# deze functie verandert een string in een list en telt de characters van elke item in de list en telt ze op en daarna deelt ze door de aantal items in de list

print(ruimte_hamsterwiel("hallo.yousef yousef"))



def spaghetti_spaceship(infinity_pizza:int, parallelle_tosti:int=10) -> None:
    for zwabber_krakeling in range(1, parallelle_tosti+1):
        laser_sandwich = zwabber_krakeling * infinity_pizza
        print(f'{zwabber_krakeling} x {infinity_pizza} = {laser_sandwich}')
# De functie spaghetti_spaceship genereert en drukt een tafel van vermenigvuldiging af voor een specifiek getal (infinity_pizza). Deze tafel wordt een aantal keer afgedrukt dat wordt bepaald door het argument parallelle_tosti
#in het gevaal dat je de aantal vermenigvuldiging is niet aan ge geven word de aan gegeven getaal vermenigvuldigt met 10


spaghetti_spaceship(5,5)


# yousef = 'yousef alkurdi is 23 jaar oud'.split()
# a = 0 
# for i in reversed(yousef):
#     a += len(i)
# b = a / len(i)



# print(len(yousef))
# print(a)
# print(b)
# print(yousef)