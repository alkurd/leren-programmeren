# Voornaam: [Jouw voornaam]
# Achternaam: [Jouw achternaam]
# Opdracht: Pizza Calculator

smal=8.50
medium=9.00
large=10.00
# Welcome message
print("Welkom bij Ghost voor pizza!")

# Ask the user to choose a pizza size
klant = input ("welke pizza wilt u hebben, smal, medium, large? ")
# Check the user's input and calculate the total cost for the chosen pizza size
while True:

    klant == "smal"
    kasa=int (input("hoeveel smalle pizza's wilt u hebben? "))
    totoal_smal=kasa*smal
    print (f"{totoal_smal:.2f}")
    klant == "medium"
    kasa=int and float(input("hoeveel medium pizza's wilt u hebben? "))
    totoal_medium=kasa*medium
    print (f"{totoal_medium:.2f}")
    klant == "large"
    kasa=int and float(input("hoeveel lareg pizza's wilt u hebben? "))
    totoal_large=kasa*large
    print (f"{totoal_large:.2f}")   
    break
totoal_pizza_prijs=totoal_smal+totoal_medium+totoal_large
# Print the receipt
print("-"*36)
print("="*15,"Bon","="*15)
print("")
print("-"*36)
print(f"smalle pizza: {smal:.2f} * {kasa} =         {totoal_smal:.2f} ")
print("-"*36)
print(f"smalle pizza: {medium:.2f} * {kasa} =       {totoal_medium:.2f} ")
print("-"*36)
print(f"smalle pizza: {large:.2f} * {kasa} =        {totoal_large:.2f} ")
print("-"*36)
print("")
print("-"*36)
print(f"totale pizza prijzen:         {totoal_pizza_prijs:.2f}   ")
print("-"*36)
