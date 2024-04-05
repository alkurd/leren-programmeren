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
print(kleur)



while True:
    kleur = input('Geef een kleur: ')

    fruit_gevonden = False
    for fruit in fruitmand:
        if get_color(fruit) == kleur:
            print(f"Naam: {fruit['name']}, Gewicht: {fruit['weight']}")
            fruit_gevonden = True
            

    if fruit_gevonden:
        break
    else:
        print(f'De kleur {kleur}, zit niet in de fruitmand.')