from functions import addition, subtraction, multiplication, division
from termcolor import colored
def perform_operation(choice, n1, n2=None):
    if choice in ['A','E']:
        result = addition(n1, n2)
        print(f"\n{n1} + {n2} = {result}\n")
        return result
    elif choice in ['B','F']:
        result = subtraction(n1, n2)
        print(f"\n{n1} - {n2} = {result}\n")
        return result
    elif choice in ['C', 'G']:
        result = multiplication(n1, n2)
        print(f"\n{n1} * {n2} = {result}\n")
        return result
    elif choice in['D','H']:
            result = division(n1, n2)
            print(f"{n1} / {n2} = {result}")
            return result
keuzen_lijst = ["Wat wilt u doen? Kies een van de volgende opties:",
                "A) getallen optellen",
                "B) getallen aftrekken",
                "C) getallen vermenigvuldigen",
                "D) getallen delen",
                "E) getal ophogen",
                "F) getal verlagen",
                "G) getal verdubbelen",
                "H) getal halveren",
                "Uw keuze: "]
letter = ['A','B','C','D','E','F','G','H']
firstRound = True
n1 = None
while True:
        if not firstRound:
            keuzen_lijst[0] = f'Wat wil je met ({colored(n1,'red')}) doen\n'
        choice = input('\n'.join(keuzen_lijst)).upper()
        if choice in letter:
            firstRound = False
            if 'S' not in letter:
                letter.append('S')
                keuzen_lijst.insert(-1, 'S) Stoppen')
            if n1 == None:
                n1 = int(input("Geef uw eerste getal: "))
            if choice in ['E','F','G','H']:
                n2 =  1 if choice in ['E','F'] else 2
            elif choice == 'S':
                print("Programma beëindigd.")
                break
            else:
                n2 = int(input("Geef uw tweede getal: "))
            result = perform_operation(choice,n1,n2)
            n1 = result
        else:
            print("Ongeldige keuze! Probeer opnieuw.")

    
        
    

#############################################################################################
    


# rekenmachine.py

# from functions import addition, subtraction, multiplication, division



# def main():
#     firstRound = True
#     n1 = False
#     voorbeeld = ['Wat wilt u doen?',
#                 'A) getallen optellen',
#                 'B) getallen aftrekken',
#                 'C) getallen vermenigvuldigen',
#                 'D) getallen delen',
#                 'E) getal ophogen',
#                 'F) getal verlagen',
#                 'G) getal verdubbelen',
#                 'H) getal halveren'
#                 ]
#     letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#     while True:
#         while True:
#             choice = input('\n'.join(voorbeeld)+'\n').upper()  
#             if choice in letters:
#                 break
#             else:
#                 print("Ongeldige keuze! Probeer opnieuw.")

#         if firstRound:
#             voorbeeld.append ('I) niets?') 
#             letters.append ('I')

#             # voorbeeld[0] = f'Wil je wat met de uitkomst ({n1}) doen?'
#             firstRound = False
#             n1 = float(input("Voer het eerste getal in: "))
#         # else:
#         #     choice = input(voorbeeld).upper()

#         if choice == 'I':
#             break
        
        

#         if choice in ['E', 'F', 'G', 'H']:
#             n2 = 1 if choice in ['E', 'F'] else 2
#         else:
#             n2 = float(input("Voer het tweede getal in: "))


#         if choice in['A','E']:
#             uitkomst = addition(n1, n2)
#             print(f"{n1} + {n2} = {uitkomst}")
#         elif choice in['B','F']:
#             uitkomst = subtraction(n1, n2)
#             print(f"{n1} - {n2} = {uitkomst}")
#         elif choice in['C','G']:
#             uitkomst = multiplication(n1, n2)
#             print(f"{n1} * {n2} = {uitkomst}")
#         elif choice in['D','H']:
#             uitkomst = division(n1, n2)
#             print(f"{n1} / {n2} = {uitkomst}")
        

#         n1 = uitkomst
#         voorbeeld[0] = f'Wil je wat met de uitkomst ({n1}) doen?'
        

# if __name__ == "__main__":
#     main()
