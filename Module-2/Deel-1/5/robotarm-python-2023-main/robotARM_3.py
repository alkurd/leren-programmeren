from RobotArm import RobotArm
robotArm = RobotArm('exercise 3')
robotArm.speed = 5
for i in range (2):
    for _ in range (1):
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()


robotArm.wait()