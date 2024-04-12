# yellow = 3
# bruin = 1
# red = 1
# orange = 1
# green = 1
from fruitmand import fruitmand

def get_color(fruit):
    return fruit['color']
kleur = []
for fruit in fruitmand:
    kleur.append(get_color(fruit))
kleur_gekozen =''
while kleur_gekozen not in kleur:
    kleur_gekozen = input('Geef een kleur: ')
    if kleur_gekozen not in kleur:
        print(f'De kleur {kleur_gekozen}, zit niet in de fruitmand.')
    else:
        ronde_vruchten = 0
        niet_ronde_vruchten = 0
        for fruit in fruitmand:
            if get_color(fruit) == kleur_gekozen:
                if fruit['round'] == True:
                    ronde_vruchten += 1
                else:
                     niet_ronde_vruchten += 1
        verschil = abs(ronde_vruchten - niet_ronde_vruchten)
        if ronde_vruchten > niet_ronde_vruchten:
            print(f'Er zijn {verschil} meer ronde vruchten dan niet-ronde vruchten in de kleur {kleur_gekozen}.')
        elif ronde_vruchten < niet_ronde_vruchten:
            print(f'Er zijn {verschil} minder ronde vruchten dan niet-ronde vruchten in de kleur {kleur_gekozen}.')
        else:
            print(f'Er zijn evenveel ronde vruchten als niet-ronde vruchten ({ronde_vruchten}) in de kleur {kleur_gekozen}.')