
import random

rounds_played = 0
continue_playing = True
score = 0

while continue_playing and rounds_played < 20:
    secret_number = random.randint(1, 1000)
    print(secret_number)
    guess_number = 0
    guess = 0
    rounds_played += 1
    print(f'Je score nu is {score}')
    print(f"\n--- Ronde {rounds_played} ---")
    while guess_number != 10:
        guess_number += 1
        guess = input(f"{guess_number}- Doe een gok tussen 1 en 1000: ")
        if guess == 'q':
            exit()
        elif int(guess) == secret_number:
            score += 1
            print("Je hebt gewonnen!")
            next_round = input('Wil je nog een rondje spelen?\n')
            if next_round.lower() != 'ja':
                continue_playing = False
                print(f'Je score nu is {score}')  # Het spel niet voortzetten
            break  # Onderbreek de binnenste lus
        else:
            difference = abs(int(guess) - secret_number)
            if difference < 20:
                if int(guess) > secret_number:
                    print("lager")
                else:
                    print('hoger')
                print("Je bent heel warm!")
            elif difference < 50:
                if int(guess) > secret_number:
                    print("lager")
                else:
                    print('hoger')
                print("Je bent warm!")
            else:
                if int(guess) > secret_number:
                    print("lager")
                else:
                    print('hoger')
                print("Koud.")
