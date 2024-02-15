from RobotArm import RobotArm
robotArm = RobotArm('exercise 5')
for _ in range (7):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for _ in range (7):
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
robotArm.wait()