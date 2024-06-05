# Variabelen
croissantjes = int(input("hoeveel croissantjes wil je hebben? "))
stokbrood = int(input("hoeveel stokbrood wil je hebben? "))
croissantjes_prijs = 39
stokbrood_prijs = 278
korting = 50
bonen = int(input("hoeveel korting bonnen heb je? "))

# Berekeningen
bedrag1 = croissantjes * croissantjes_prijs
bedrag2 = stokbrood * stokbrood_prijs
bedrag3 = korting * bonen
totaal_bedrag = bedrag1 + bedrag2 - bedrag3
totaal = totaal_bedrag/100

# Bonafdruk
print("------------------------------")
print("        Bon - Bakkerij")
print("------------------------------")
print(f"{croissantjes} Croissantjes  €{croissantjes_prijs/100:.2f}:       €{bedrag1/100:.2f}")
print(f"{stokbrood} Stokbroden  €{stokbrood_prijs/100:.2f}:           €{bedrag2/100:.2f}")
print(f"Korting ({bonen} bonnen  €{korting/100:.2f}):               €{bedrag3/100:.2f}")
print("------------------------------------- +")
print(f"Totaal:                               €{totaal:.2f}")
print("-------------------------------------")
print(f"De feestlunch kost je bij de bakker {totaal} euro voor de {croissantjes} croissantjes en de {stokbrood} stokbroden als de {bonen} kortingsbonnen nog geldig zijn!")