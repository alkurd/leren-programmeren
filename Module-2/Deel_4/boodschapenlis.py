boodschappenlijst = {}
while True:
    boodschap = input('Voeg een boodschap toe:\n').strip() .lower()
    if boodschap.isdigit():
        print("Ongeldige invoer, voer een productnaam in!")
        continue

    if boodschap == 'q':
        break
    aantal = int(input(f'Hoeveel {boodschap} wil je hebben? '))
    if boodschap in boodschappenlijst:
        boodschappenlijst[boodschap] += aantal
    else:
        boodschappenlijst[boodschap] = aantal
print("Boodschappenlijst:")
for boodschap in boodschappenlijst:
    print(f"{boodschappenlijst[boodschap]} x {boodschap}")