from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
robotArm.grab()
for q in range (5):
    robotArm.moveRight()
robotArm.drop()
for w in range(4):
    robotArm.moveLeft()
robotArm.wait()