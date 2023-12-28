def vraag_getal(aantal):
    antwoord = input("Voer het {} getal in: ".format(aantal))
    return int(antwoord)

getal_1 = vraag_getal("eerste")
getal_2 = vraag_getal("tweede")

def vergelijker(a:int,b:int) ->str:

#statment
    if a > b:

        return('{} is groter dan  {}'.format(a,b))
    elif a < b:

        return('{} is kleiner dan {}'.format(a,b))
    else:
        return("{} is gelijk aan {}".format(a,b))
print(vergelijker(getal_1,getal_2))
#print's
# print(f'a is het maximum {MAX}')
# print(f'b is het minmum {MIN}')