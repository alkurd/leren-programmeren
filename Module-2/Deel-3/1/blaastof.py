from time import sleep
timer  = 30
while timer > 0:
    print(timer)
    sleep(0.1)
    timer -= 1
    if timer == 3:
        while timer > 0:
            print('lansiring over',timer)
            sleep(0.3)
            timer -= 1
            if timer == 0:
                print('!!!!!!!!!!blastoff!!!!!!!!!!')
                break



# from time import sleep

# timer  = 30
# while timer > 0:
#     if timer <= 3:
#         print('lansiring over', timer)
#         if timer == 1:
#             print('!!!!!!!!!!blastoff!!!!!!!!!!')
#     else:
#         print(timer)
#     sleep(0.1)
    # timer -= 1