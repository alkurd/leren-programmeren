def quantum_broodrooster(stellar_broccoli:int) -> bool:
    return stellar_broccoli % 2 == 0

# deze functie neemt de parameter als een invoer en rtuneert een boeling (True ale het even is en False ales eht oneven is )
# resultaat = quantum_broodrooster(int(input('geef en getaal: ')))
# print(resultaat)

def chaos_papegaai(fantasie_platypus:str) -> str:
    betoverde_druif = fantasie_platypus.split()
    doldwaze_broccoli = betoverde_druif[::-1]
    tijdmachine_pannenkoekenmix = ' '.join(doldwaze_broccoli)
    return tijdmachine_pannenkoekenmix
# print(chaos_papegaai("hallo yousef ik yous.")) 
# deze functie draait de string worden agterste voren

def kosmische_koekjesmix(galactische_snoepjes:str) -> int:
    planetair_taartje = set(galactische_snoepjes)
    whatchamacallit = len(planetair_taartje)
    return whatchamacallit
# input_string = input('Voer een string in: ')
resultaat = kosmische_koekjesmix('input_string')
print("Het aantal unieke karakters is:", resultaat)                              

def ruimte_hamsterwiel(planetair_taartje:str) -> float:
    wobbelwobbel = planetair_taartje.split()
    
    blork = 0
    for snorkelwagen in wobbelwobbel:
        blork += len(snorkelwagen)

    bizarro_matrix = blork / len(wobbelwobbel)
    return bizarro_matrix

def spaghetti_spaceship(infinity_pizza:int, parallelle_tosti:int=10) -> None:
    for zwabber_krakeling in range(1, parallelle_tosti+1):
        laser_sandwich = zwabber_krakeling * infinity_pizza
        print(f'{zwabber_krakeling} x {infinity_pizza} = {laser_sandwich}')