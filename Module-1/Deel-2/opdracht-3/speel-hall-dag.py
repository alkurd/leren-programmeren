# Variabelen
entree = 7.45
personen = int(input("met hoeveel man zijn jullie? "))
Gewenste_speel_tijd = int(input("hoe lang willen jullie spellen? "))
Kosten_per_5_minuten = 0.37
speel_tijd_per_35_cent = 5

# Berekeningen
kosten_entree = entree * personen
aantal_betalingen_VR_game = Gewenste_speel_tijd / speel_tijd_per_35_cent
totale_kosten_VR_game = aantal_betalingen_VR_game * personen * Kosten_per_5_minuten
totale_kosten = totale_kosten_VR_game + kosten_entree

# Boninformatie
extra_kosten = 1.32
totaal_bedrag = round(totale_kosten + extra_kosten, 2)

# Bonafdruk
print("-"*35)
print("    Bon voor een dagje uit")
print("-"*35)
print(f"Entree ({personen} personen):           €{kosten_entree:.2f}")
print(f"VR-game ({Gewenste_speel_tijd} minuten): €{totale_kosten_VR_game:.2f}")
print("-"*35)
print(f"Totaal:                               €{totaal_bedrag:.2f}")
print("-"*35)
print(f"Dit geweldige dagje-uit met {personen} mensen in de Speelhal met {Gewenste_speel_tijd} minuten VR kost je maar €{totaal_bedrag}")
