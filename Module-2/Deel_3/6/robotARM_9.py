from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
for stapel in range (1, 5):
    for blokje in range (stapel):
        robotArm.grab()
        for _ in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for a in range(4):
            robotArm.moveLeft()
        if stapel != blokje + 1:
            robotArm.moveLeft()
robotArm.wait()
            # for a in range(5):
        # if stapel == (blokje + 1)else 5 ):

# hoogte = 0

# for stapel in range (5):
#     for blokje in range (hoogte):
#         robotArm.grab()
#         for _ in range(5):
#             robotArm.moveRight()
#         robotArm.drop()
#         for _ in range(4 if hoogte == (blokje + 1) else 5):
#             robotArm.moveLeft()
#     hoogte += 1
    #     for j in range(5):
    #         robotArm.moveRight()
    #         robotArm.drop()

# robotArm.drop()
# for w in range(4):
#     robotArm.moveLeft()

    # robotArm.moveRight()

# sum = 100
# for x in range (1,sum):
#     print (x)
    # sum = 50
