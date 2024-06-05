
# Importeer random module

# rounds_played <- 0
# continue_playing <- True
# score <- 0

# Terwijl continue_playing en rounds_played < 20:
#     secret_number <- willekeurig getal tussen 1 en 1000
#     print(secret_number)
#     guess_number <- 0
#     guess <- 0
#     rounds_played += 1
#     print "Je score nu is " + score
#     print " --- Ronde " + rounds_played + " ---"
    
#     Terwijl guess_number != 10:
#         guess_number += 1
#         guess <- invoer van gebruiker (tussen 1 en 1000)
#         Als guess == 'q':
#             Exit()
#         Anders als int(guess) == secret_number:
#             score += 1
#             Print "Je hebt gewonnen!"
#             next_round <- invoer van gebruiker ('Wil je nog een rondje spelen?')
#             Als next_round.lower() != 'ja':
#                 continue_playing <- False
#                 Print "Je score nu is " + score
#             Breek  # Onderbreek de binnenste lus
#         Anders:
#             difference <- absolute waarde van (int(guess) - secret_number)
#             Als difference < 20:
#                 Als int(guess) > secret_number:
#                     Print "lager"
#                 Anders:
#                     Print "hoger"
#                 Print "Je bent heel warm!"
#             Anders als difference < 50:
#                 Als int(guess) > secret_number:
#                     Print "lager"
#                 Anders:
#                     Print "hoger"
#                 Print "Je bent warm!"
#             Anders:
#                 Als int(guess) > secret_number:
#                     Print "lager"
#                 Anders:
#                     Print "hoger"
#                 Print "Koud."
