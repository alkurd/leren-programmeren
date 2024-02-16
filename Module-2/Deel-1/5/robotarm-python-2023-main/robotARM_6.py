# from RobotArm import RobotArm
# robotArm = RobotArm('exercise 6')

# #     robotArm.moveRight()
# #     robotArm.grab()
# #     robotArm.moveLeft()
# #     robotArm.drop()
# #     # eerste blok
# #     robotArm.moveRight()
# #     robotArm.grab()
# #     robotArm.moveRight()
# #     robotArm.drop()
# #     #tweede blok
# #     robotArm.moveLeft()
# #     robotArm.grab()
# #     robotArm.moveLeft()
# #     robotArm.drop()
# # robotArm.moveRight()
# # robotArm.grab()

# # color = robotArm.scan()    
# # if color == 'white':
# #     robotArm.moveLeft()
# #     robotArm.drop()

# # else:
# #     robotArm.moveRight()
# #     robotArm.drop()
# # robotArm.moveLeft()


# # for _ in range(3):
# #     robotArm.moveRight()
# #     robotArm.grab()
# #     robotArm.moveLeft()
# #     robotArm.grab()
# # for _ in range (1):
# #     robotArm.moveRight()
# #     robotArm.grab()
# # for _ in range (2):
# #     color = robotArm.scan()
# #     if color == 'red':
# #         robotArm.moveRight()
# #         robotArm.drop()
# #         robotArm.moveLeft()
# #     else:   
# #         robotArm.moveLeft()
# #         robotArm.drop()
# #     robotArm.moveRight()
# #     robotArm.grab()
# robotArm.moveRight()
# for _ in range (6):
#     robotArm.grab()
#     color = robotArm.scan()
#     if color == 'white':
#         robotArm.moveLeft()
#         robotArm.drop()
#         robotArm.moveRight()
#     else:
#         robotArm.moveRight()
#         robotArm.drop()
#         robotArm.moveLeft()
# robotArm.wait()

def switch_boolean(lst):
    result = []
    switch = True
    for item in lst:
        if item == 'flick':
            switch = not switch
        result.append(switch)
    return result

# Test cases
print(switch_boolean(['codewars', 'flick', 'code', 'wars']))
print(switch_boolean(['flick', 'chocolate', 'adventure', 'sunshine']))
print(switch_boolean(['bicycle', 'jarmony', 'flick', 'sheep', 'flick']))
