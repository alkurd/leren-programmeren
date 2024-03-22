from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')

for i in range (5):
    robotArm.grab()
    for j in range (9 - (i *2)):
        robotArm.moveRight()
    # a -= 2
    robotArm.drop()
    for j in range (8 - (i *2)):
        robotArm.moveLeft()
  
robotArm.wait()