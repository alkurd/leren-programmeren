# def list_maker (lengte, stap):
#     return [ A * stap for A in range (1, lengte + 1) ]

# def main():
#     aantallijsten = int(input('hoeveel lijsten wil je hebben'))
#     lijstjes = []

#     for i in range (1, aantallijsten +1):
#         lengte = int (input(f'hoeveel in lijst {i}'))
#         lijstjes.append(list_maker(lengte, i))
#     print(lijstjes)

# if __name__ == '__name__':
#     main()



# aantal_lijstjes = int(input("Hoeveel lijstjes? "))
# lijstjes = []
    
# for i in range(1, aantal_lijstjes + 1):
#     lengte = int(input(f"Hoeveel in lijst {i}? "))
#     lijstjes = [0] * lengte
    
#     print(lijstjes)




# def list_maker(lengte, stap):
#     return [0] * lengte
# def main():
#     aantal_lijstn = int(input('Hoeveel lijsten? '))
#     lijsten = []

#     for a in range (1,aantal_lijstn + 1):
#         lengte = int(input(f'Hoeveel in lijst {a}? '))
#         lijsten.append(list_maker(lengte, a))
#         print (lijsten)
# if __name__ == '__name__':
#     main()


# fruit = ['appel', 'banaan', 'peren']

# type(fruit)
# print (type(fruit))
# fruit = []
# fruit.append('APPEL')
# fruit.append('piren')
# print(fruit)

# groente= []
# groente.append('totmaal')
# groente.append('sla')
# print(groente)

# leters = []
# leters.append('1')
# leters.append('2')
# print(leters)

# A = []
# A.append(fruit)
# A.append(groente)
# A.append(leters)
# print(A)

# aantal_lijsten = []
# aantal_lijstjes = int(input("Hoeveel lijstjes? "))
# lijsten = []
# a = []
# for lijsten in range (1,aantal_lijstjes + 1) :
#     inhoud_lijst = int(input(f'hoeveel in lijst {lijsten}? '))
#     [a * lijsten ]
#     lijsten .append (aantal_lijsten)
#     # for aantal_lijsten in lijsten:





# print(f'{aantal_lijsten}')

# A = []
# aantal = 4
# vactor = 2
# for x in range (aantal):
#     y = (x + 1 ) * vactor
#     print (y )
#     A.append(y)
# print(A)
    

# def first_liste(A_lijst,B_lijsten):
#     return A_lijst.append(B_lijsten)


# A_lijst = int(input('hoeveel lijsten wilt u hebben? '))

# for i in range(1, + 1):
#     inner_lijst = int(input(f'hoeveel wilt u hebben in list {i}'))
# print()


# for B_lijst in range (1, A_lijst + 1):
#     C_lijst = int(input(f'hoeveel wilt u hebben in lijste {B_lijst}? '))
# klein_lijst = [C_lijst]
# lijst.append(klein_lijst)
# print(klein_lijst)



# input_int = int(input("Voer een integer in: ")

# # Maak een lijst met één element, de ingevoerde integer
# lijst = [input_int]

# # Print de resulterende lijst
# print("De ingevoerde lijst is:", lijst)


lijst = []
aantal_listen = int(input('hoeveel lijsten wilt u hebben? '))
# lijst.append(aantal_listen)
for list_nummer in range (1, aantal_listen + 1):
    inner_lijst = int(input(f'hoeveel wilt u hebben in list nummer {list_nummer}?'))
    steps = [ i * list_nummer for i in range(1, inner_lijst + 1)]
    lijst.append(steps)
print( lijst)


# # Vraag het aantal lijsten
# aantal_lijsten = int(input("Hoeveel lijstjes? "))

# # Lijst van lijsten
# lijsten = []

# # Loop door het aantal lijsten
# for lijst_nummer in range(1, aantal_lijsten + 1):
#     # Vraag het aantal elementen in de huidige lijst
#     aantal_elementen = int(input(f"Hoeveel in lijst {lijst_nummer}? "))
    
#     # Maak een lijst met getallen van 1 tot en met het aantal elementen vermenigvuldigd met het lijstnummer en voeg deze toe aan de lijst van lijsten
#     sublist = [j * lijst_nummer for j in range(1, aantal_elementen + 1)]
#     lijsten.append(sublist)

# # Print de resulterende lijsten
# print("De ingevoerde lijsten zijn:", lijsten)
