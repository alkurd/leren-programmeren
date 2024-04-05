from fruitmand import fruitmand

vertaling = {'red':'rode',
            'green':'groen',
            'yellow':'geel',
            'orange':'oranje',
            'white':'wit',
            'brown':'bruin',
            'blue':'blauw',
            'purple':'paars',
            'pink':'roos',
            'black':'zwart'}
def get_letter_length(length):
    return len(length['name'])
def vertaal_kleur(kleur):
    if kleur in vertaling:
        return vertaling[kleur]
  
get_info = max(fruitmand, key=get_letter_length)
kleur_vertaald = vertaal_kleur(get_info['color'])

print(f"De {get_info['name']} heeft {len(get_info['name'])} letters en heeft de kleur {kleur_vertaald} en een gewicht van {get_info['weight']} kg.")


#print(f"De {fruit['name']} heeft {len(fruit['name'])} letters en heeft de kleur {vertaal_kleur(fruit['color'])} en een gewicht van {fruit['weight']} kg.")