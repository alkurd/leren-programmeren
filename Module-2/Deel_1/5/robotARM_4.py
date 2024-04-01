from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')
# de eerste 4 blokjes 2 keer naar rechts
for stapel in range(4):
    robotArm.grab()
    for a in range (2):
        robotArm.moveRight()
    robotArm.drop()
    for _ in range (2):
        robotArm.moveLeft()
# lateste blok een keer rechts
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
# de stapel van de derde kolom terug stapelen naar de tweede kolom
for stapel in range (4):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
robotArm.moveLeft()
robotArm.wait()
