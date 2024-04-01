from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
for stapel in range (5):
    for blokjes in range (6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    if stapel < 4:
        for _ in range (2):
            robotArm.moveRight()
robotArm.wait()
    # print(stapel)