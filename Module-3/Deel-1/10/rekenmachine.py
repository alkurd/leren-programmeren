from functions import addition, subtraction, multiplication, division, increment, decrement, double, halve, square, cube, square_root, cube_root, factorial

def perform_operation(choice, a, b=None):
    if choice == "A":
        result = addition(a, b)
        print(f"\n{a} + {b} = {result}\n")
        return result
    elif choice == "B":
        result = subtraction(a, b)
        print(f"\n{a} - {b} = {result}\n")
        return result
    elif choice == "C":
        result = multiplication(a, b)
        print(f"\n{a} * {b} = {result}\n")
        return result
    elif choice == "D":
        result = division(a, b)
        if isinstance(result, str):
            print(result)
        else:
            print(f"\n{a} / {b} = {result}\n")
        return result
    elif choice == "E":
        result = increment(a)
        print(f"\n{a} + 1 = {result}\n")
        return result
    elif choice == "F":
        result = decrement(a)
        print(f"\n{a} - 1 = {result}\n")
        return result
    elif choice == "G":
        result = double(a)
        print(f"\n{a} * 2 = {result}\n")
        return result
    elif choice == "H":
        result = halve(a)
        print(f"\n{a} / 2 = {result}\n")
        return result
    elif choice == 'I':
        result = square(a)
        print(f"\n{a} ^ 2 = {result}\n")
        return result
    elif choice == 'J':
        result = cube(a)
        print(f"\n{a} ^ 3 = {result}\n")
        return result
    elif choice == 'K':
        result = square_root(a)
        print(f"\n√{a} = {result}\n")
        return result
    elif choice == 'L':
        result = cube_root(a)
        print(f"\n∛{a} = {result}\n")
        return result
    elif choice == 'M':
        result = factorial(a)
        print(f"\n{a}! = {result}\n")
        return result
# StopWorden = ["stop", "nee", "niet", "genoeg", "klaar", "exit", "afsluiten"]
while True:
    choice = input("Wat wilt u doen? Kies een van de volgende opties:\n"
                "A) getallen optellen\n"
                "B) getallen aftrekken\n"
                "C) getallen vermenigvuldigen\n"
                "D) getallen delen\n"
                "E) getal ophogen\n"
                "F) getal verlagen\n"
                "G) getal verdubbelen\n"
                "H) getal halveren\n"
                "I) getal kwadraat\n"
                "J) getal kubus\n"
                "K) vierkantswortel\n"
                "L) derdemachtswortel\n"
                "M) faculteit\n"
                "S) stopen\n"
                "Uw keuze: ").upper()

    if choice in ['A', 'B', 'C', 'D']:
            a = float(input("Voer het eerste getal in: "))
            b = float(input("Voer het tweede getal in: "))
            result = perform_operation(choice, a, b)
    elif choice == 'S':
         print("Bedankt voor het gebruiken van de calculator. Tot ziens!")
         exit()
    elif choice in ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']:
            a = float(input("Voer het getal in: "))
            result = perform_operation(choice, a)
    # print()
    # print("--------------------------------")
    # print(f"Het resultaat is: {result}")
    # print("--------------------------------")
    # print()
    while True:
        next_choice = input(f'Wil je wat met {result} doen?\n'
                            'A) Iets optellen\n'
                            'B) Iets aftrekken\n'
                            'C) Iets vermenigvuldigen\n'
                            'D) Ergens door delen\n'
                            'E) Ophogen\n'
                            'F) Verlagen\n'
                            'G) Verdubbelen\n'
                            'H) Halveren\n'
                            'I) Kwadraat\n'
                            'J) Kubus\n'
                            'K) Vierkantswortel\n'
                            'L) Derdemachtswortel\n'
                            'M) Faculteit\n'
                            'N) Nieuwe getallen invoeren\n'
                            "S) stopen\n"
                            'Uw keuze: ').upper()
        if next_choice in ['A', 'B', 'C', 'D']:
                b = float(input("Voer het tweede getal in: "))
                result = perform_operation(next_choice, result, b)
        elif next_choice in ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']:
                result = perform_operation(next_choice, result)
        elif next_choice =='N':
            break
        elif next_choice == 'S':
            print("Bedankt voor het gebruiken van de calculator. Tot ziens!")
            exit()
    print()
    print("--------------------------------")
    print(f"Het resultaat is: {result}")
    print("--------------------------------")
    print()

#############################################################################################
    


# # rekenmachine.py
# from functions import addition, subtraction, multiplication, division

# def get_number_input(prompt):
#     return float(input(prompt))

# def main():
#     firstRound = True
#     n1 = False

#     while True:
#         if firstRound:
#             choice = input('Wat wilt u doen?\n'
#                            'A) getallen optellen\n'
#                            'B) getallen aftrekken\n'
#                            'C) getallen vermenigvuldigen\n'
#                            'D) getallen delen\n'
#                            'E) getal ophogen\n'
#                            'F) getal verlagen\n'
#                            'G) getal verdubbelen\n'
#                            'H) getal halveren\n')
                            
#             firstRound = False
#         else:
#             choice = input(f"Wil je wat met de uitkomst ({uitkomst}) doen?\n"
#                            'A) iets optellen\n'
#                            'B) iets aftrekken\n'
#                            'C) met iets vermenigvuldigen\n'
#                            'D) ergens door delen\n'
#                            'E) ophogen\n'
#                            'F) verlagen\n'
#                            'G) verdubbelen\n'
#                            'H) halveren\n'
#                            'I) niets?\n')

#         if choice.upper() == 'I':
#             break
        
#         if n1 == False:
#             n1 = get_number_input("Voer het eerste getal in: ")

#         if choice.upper() in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
#             if choice.upper() in ['E', 'F', 'G', 'H']:
#                 n2 = 1 if choice.upper() in ['E', 'F'] else 2
#             else:
#                 n2 = get_number_input("Voer het tweede getal in: ")

#         if choice.upper() == 'A':
#             uitkomst = addition(n1, n2)
#             print(f"{n1} + {n2} = {uitkomst}")
#         elif choice.upper() == 'B':
#             uitkomst = subtraction(n1, n2)
#             print(f"{n1} - {n2} = {uitkomst}")
#         elif choice.upper() == 'C':
#             uitkomst = multiplication(n1, n2)
#             print(f"{n1} * {n2} = {uitkomst}")
#         elif choice.upper() == 'D':
#             uitkomst = division(n1, n2)
#             print(f"{n1} / {n2} = {uitkomst}")
#         elif choice.upper() == 'E':
#             uitkomst = addition(n1, n2)
#             print(f"{n1} + {n2} = {uitkomst}")
#         elif choice.upper() == 'F':
#             uitkomst = subtraction(n1, n2)
#             print(f"{n1} - {n2} = {uitkomst}")
#         elif choice.upper() == 'G':
#             uitkomst = multiplication(n1, n2)
#             print(f"{n1} * {n2} = {uitkomst}")
#         elif choice.upper() == 'H':
#             uitkomst = division(n1, n2)
#             print(f"{n1} / {n2} = {uitkomst}")
#         else:
#             print("Ongeldige keuze! Probeer opnieuw.")

#         n1 = uitkomst

# if __name__ == "__main__":
#     main()
