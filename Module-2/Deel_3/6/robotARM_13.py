from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)
for z in range (7):
    robotArm.grab()
    color = robotArm.scan()
    if color !='':
        for i in range (1 + z ):
            robotArm.moveRight()
            i -= 1
        robotArm.drop()
        for i in range (1 + z ):
            robotArm.moveLeft()
    else:
        break
robotArm.wait()

