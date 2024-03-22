from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')

hoogte = 1

for stapel in range (4):
    for blokje in range (hoogte):
        robotArm.grab()
        for _ in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for _ in range(4 if hoogte == (blokje + 1) else 5):
            robotArm.moveLeft()
    hoogte += 1
    #     for j in range(5):
    #         robotArm.moveRight()
    #         robotArm.drop()

# robotArm.drop()
# for w in range(4):
#     robotArm.moveLeft()
robotArm.wait()
# sum = 100
# for x in range (1,sum):
#     print (x)
    # sum = 50
