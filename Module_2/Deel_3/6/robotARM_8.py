from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.moveRight()
for _ in range (7):
    robotArm.grab()
    for _ in range (8):
        robotArm.moveRight()
    robotArm. drop()
    for _ in range (8):
        robotArm.moveLeft()
robotArm.wait()