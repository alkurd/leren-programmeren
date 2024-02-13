from time import sleep

def slow_print(tekst,snelheid =0.05):
    for karakter in tekst:
        print(karakter, end='', flush=True)
        sleep(snelheid)
    print()

def slow_input(prompt):
    slow_print(prompt)
    return input()




# def get_chois(story:str, prompt:str ,option:list) ->str:
#     slow_print(story)
#     while True:
#         answor = slow_input(prompt+f'{(" of ").join(option)}')
#         if answor in option:
#             return answor
#         else:
#             print('worng answer')