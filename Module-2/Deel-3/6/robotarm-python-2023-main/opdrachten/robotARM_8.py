from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.moveRight()
for _ in range (7):
    for _ in range (1):
        robotArm.grab()
        for _ in range (8):
            robotArm.moveRight()
        robotArm. drop()
        for _ in range (8):
            robotArm.moveLeft()
robotArm.wait()