# import random
# secret_number = random.randint(1, 1000)
# score = 0
# rounds_played = 0
# print(secret_number)
# while rounds_played < 20:
#     rounds_played += 1
#     print(f"\n--- Ronde {rounds_played} ---")
#     guess = int(input("Doe een gok tussen 1 en 1000: "))
#     if guess == secret_number:
#         print("Je hebt gewonnen!")
#         score += 1
#         break
#     else:
#         difference = abs(guess - secret_number)
#         if difference < 20:
#             print("Je bent heel warm!")
#         elif difference < 50:
#             print("Je bent warm!")
#         else:
#             print("Het getal is niet erg warm.")

#     score += 1
    
#     print(f"Huidige score: {score}")
    
#     if rounds_played < 20:
#         play_again = input("Nog een getal raden? (ja/nee): ").lower()
#         if play_again != 'ja':
#             break
# else:
#     print("Maximaal aantal rondes bereikt.")

# print(f"Eindscore: {score}")
# print(difference)

import random
secret_number = random.randint(1, 1000)
rounds_played = 0
guss = 0
print(secret_number)
while rounds_played < 20:
    print(f"\n--- Ronde {rounds_played} ---")
    while guss != secret_number:
        guss = input("Doe een gok tussen 1 en 1000: ")
        if guss == 'q':
            exit()
        elif guss == secret_number:
            print("Je hebt gewonnen!")
            next_round = input('Wil je nog een rondje spelen?\n')
            rounds_played += 1
            break
        else:
            difference = abs(int(guss) - secret_number)
            if difference < 20:
                print("Je bent heel warm!")
            elif difference < 50:
                print("Je bent warm!")
            else:
                print("Koud.")