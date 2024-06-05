# Variabelen
entree = 7.45
personen = 4
gewenste_speel_tijd = 45
kosten_per_5_minuten = 0.37
speel_tijd_per_rondje = 5

# Berekeningen
kosten_entree = entree * personen
aantal_betalingen_VR_game = gewenste_speel_tijd / speel_tijd_per_rondje
totale_kosten_VR_game = aantal_betalingen_VR_game * personen * kosten_per_5_minuten
totale_kosten = totale_kosten_VR_game + kosten_entree

# Boninformatie

totaal_bedrag = (f'{totale_kosten:.2f}')

# Bonafdruk
print("-" * 35)
print("    Bon voor een dagje uit")
print("-" * 35)
print(f"Entree ({personen} personen):           €{kosten_entree:.2f}")
print(f"VR-game ({gewenste_speel_tijd} minuten): €{totale_kosten_VR_game:.2f}")
print("-" * 35)
print(f"Totaal:                               €{totaal_bedrag:.2f}")
print("-" * 35)
print(f"Dit geweldige dagje-uit met {personen} mensen in de Speelhal met {gewenste_speel_tijd} minuten VR kost je maar €{totaal_bedrag}")
