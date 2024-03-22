from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
for _ in range (9):
    robotArm.moveRight()
for _ in range (9):
    robotArm.moveLeft()
    robotArm.grab()
    clolor = robotArm.scan()
    if clolor == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
robotArm.wait()
# blokjes = 8
# kleur = 0 
# for  a in range (blokjes):
#     robotArm.grab()
#     color = robotArm.scan()
#     if color == 'white':
#         robotArm.moveRight()
#         robotArm.drop()
#         robotArm.moveRight()
#         blokjes -=  1
#         if blokjes - 1 :
#             kleur += 1
#         if kleur == 2:
#             blokjes -= 3
#         print(blokjes) 
#         print(kleur)
#     else:
#         robotArm.drop()
#         robotArm.moveRight()