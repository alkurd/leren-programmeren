import random
kleuren = ['rood', 'blauw', 'groen', 'geel', 'paars']
zak_mm = {}
klant = int(input('hoeveel mms wilt je hebben? '))
for mm in range(klant):
    kleur = random.choice(kleuren)
    if kleur  in  zak_mm:
        # zak_mm[kleur] = 0 
        zak_mm[kleur] +=1
    else:
        zak_mm[kleur] = 1
    # mijn_dict[kleur] = mijn_dict.get(kleur,0) + 1 

print("De resulterende dictionary met de zak met M&M's is:")
print(zak_mm)
for _ in zak_mm:
    print(f"{_}: {zak_mm[_]}")



