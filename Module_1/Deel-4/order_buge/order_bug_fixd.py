def vraag_getal(aantal):
    antwoord = input("Voer het {} getal in:".format(aantal))
    getal = int(antwoord)
    return getal

getal_1 = vraag_getal("eerste")
getal_2 = vraag_getal("tweede")


def deel_getallen(a, b):
    antwoord = print(a / b)
    return antwoord
    
if getal_1 == 0:
    print("Kan niet delen door 0")
else:
    resultaat = deel_getallen(getal_1, getal_2)
    print ("{} gedeeld door {} is gelijk aan {}".format(getal_1, getal_2, resultaat))
    





