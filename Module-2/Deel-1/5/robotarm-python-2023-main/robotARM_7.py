from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
for _ in range (5):
    for _ in range (6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for _ in range (2):
        robotArm.moveRight()

robotArm.wait()