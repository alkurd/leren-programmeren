# Variabelen
croissantjes = 17
stokbrood = 2
croissantjes_prijs = 0.39
stokbrood_prijs = 2.78
korting=-0.50
bonen=3

# Berekeningen
bedrag1=croissantjes*croissantjes_prijs
bedrag2=stokbrood*stokbrood_prijs
bedrag3=korting*bonen
totaal_bedrag=bedrag1+bedrag2+bedrag3

# Bonafdruk
print("------------------------------")
print("        Bon - Bakkerij")
print("------------------------------")
print(f"{croissantjes} Croissantjes  €{croissantjes_prijs:.2f}:       €{bedrag1:.2f}")
print(f"{stokbrood} Stokbroden  €{stokbrood_prijs:.2f}:           €{bedrag2:.2f}")
print(f"Korting ({bonen} bonnen  €{korting:.2f}):               €{bedrag3:.2f}")
print("------------------------------------- +")
print(f"Totaal:                               €{totaal_bedrag:.2f}")
print("-------------------------------------")
print("De feestlunch kost je bij de bakker", totaal_bedrag, "euro voor de", croissantjes, "croissantjes en de", stokbrood, "stokbroden als de", bonen, "kortingsbonnen nog geldig zijn!")