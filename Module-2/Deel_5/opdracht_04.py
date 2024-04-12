from fruitmand import fruitmand
import random

gebruiker = int(input('aantal fruit?\n'))
for i in range(gebruiker):
    print(f"{i+1}. {fruitmand[random.randint(0,len(fruitmand)-1)]['name']}")
    