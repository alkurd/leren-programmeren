import random

kleuren_M_en_M = ('Oranje','Blouw','Groen','Bruin','paars')
mms = []
aantal_mms = int(input("Hoeveel M&M wil je hebben?" ))

for _ in range(aantal_mms) :
    # random_kleur = random.randint(0, len(kleuren_M_en_M) - 1)
    random_kleur = random.randint(0,len(kleuren_M_en_M) - 1)
    if random_kleur == 3:
        random_kleur = 2
    # print(len(kleuren_M_en_M))
    # print()
    # print(random_kleur)
    kleuren = kleuren_M_en_M [random_kleur]
    mms.append(kleuren)
print(mms)




# def zak_met_mm(list):
#     lege_list = list
# import random

# kleuren_tupel = ("rood", "blauw", "groen", "geel", "paars")

# for kleur in kleuren_tupel:
#     random_index = random.randint(0, len(kleuren_tupel) - 1)
#     willekeurige_kleur = kleuren_tupel[random_index]
#     print("Is", willekeurige_kleur, "een van je favoriete kleuren?")