# Case_3
# Developers: Zhambaldorzhieva A., Ryaguzova D., Zaitseva D.
#
import ru_local as ru
import random


def random_granny():
    rand_granny = random.choice([1, 2])
    return rand_granny


def floor2():
    health = 3
    force = 5
    print(f'{ru.CHOOSE}:\n1.{ru.GO}\n2.{ru.ENTER}')
    act = int(input(f'{ru.ACT}->'))
    if act == 1:
        if random_granny() == 2:
            print(f'{ru.OH_OH}')
            health -= 1
            force -= 2
        print(f'{ru.CHOOSE}:\n1.{ru.GO_TO_ROOM_1}\n2.{ru.GO_TO_ROOM_2}')
        act_1 = int(input(f'{ru.ACT}->'))
        if act_1 == 1:
            print(f'{ru.CHOOSE}:\n1.{ru.OPEN_WARDROBE}\n2.{ru.OPEN_FRIDGE}')
            act_2 = int(input(f'{ru.ACT}->'))
            if act_2 == 1:
                print(ru.EMPTY)
            else:
                print(ru.SPRAY)
        else:
            print(ru.EMPTY)
        print(f'{ru.CHOOSE}:\n1.{ru.GO}\n2.{ru.GO_TO_ROOM_1}')
        act_3 = int(input(f'{ru.ACT}->'))
        if act_3 == 1:
            if random_granny() == 2:
                print(f'{ru.OH_OH}')
                health -= 1
                force -= 2
            print(f'{ru.CHOOSE}:\n1.{ru.GO}\n2.{ru.GO_TO_ROOM_3}')
            act_4 = int(input(f'{ru.ACT}->'))
            if act_4 == 1:
                if random_granny() == 2:
                    print(f'{ru.OH_OH}')
                    health -= 1
                    force -= 2
            else:
                print(f'{ru.CHOOSE}:\n1.{ru.OPEN_WARDROBE}\n2.{ru.OPEN_BAG}')
                act_5 = int(input(f'{ru.ACT}->'))
                if act_5 == 1:
                    print(f'{ru.MEDICINE}')
                    health += 1
                    if health > 3:
                        health = 3
                else:
                    print(f'{ru.EMPTY}')
        else:
            print(f'{ru.CHOOSE}:\n1.{ru.OPEN_WARDROBE}\n2.{ru.OPEN_FRIDGE}')
            act_2 = int(input(f'{ru.ACT}->'))
            if act_2 == 1:
                print(f'{ru.EMPTY}')
            else:
                print(f'{ru.SPRAY}')
    else:
        print(f'{ru.CHOOSE}:\n1.{ru.OPEN_WARDROBE}\n2.{ru.OPEN_BAG}')
        act_5 = int(input(f'{ru.ACT}->'))
        if act_5 == 1:
            print(f'{ru.MEDICINE}')
            health += 1
            if health > 3:
                health = 3
    return force


def floor_1():
    health = 3
    force = 5
    for j in names:
        print(f'{j}, {ru.CHOOSE}:\n1.{ru.KITCHEN}\n2.{ru.GO}\n3.{ru.EXIT}')
        act_1 = int(input(f'{ru.ACT}->'))
        if act_1 == 1:
            print(f'{ru.KITCHEN_PL} {ru.CHOOSE}:\n1.{ru.OPEN_FRIDGE}\n2.{ru.OPEN_WARDROBE}')
            act_2 = int(input(f'{ru.ACT}->'))
            if act_2 == 1:
                print(f'{ru.EAT}')
                if force < 5:
                    force += 1
                else:
                    force = 5
            else:
                print(f'{ru.EMPTY}\n{ru.RETURN}\n1.{ru.GO}\n2.{ru.EXIT}')
                act_3 = int(input(f'{ru.ACT}->'))
                if act_3 == 1:
                    if random_granny() == 1:
                        health -= 1
                        force -= 2
                        print(f'{ru.GRANNY_BAD}\n{ru.RESOURCES}'
                              f'\n{ru.HEALTH}: {health} \n{ru.FORCE}: {force}')
                    else:
                        print(f'{ru.CLOSE_DOOR}')
        elif act_1 == 2:
            if random_granny() == 1:
                health -= 1
                force -= 2
                print(f'{ru.GRANNY_BAD}\n{ru.RESOURCES}'
                      f'\n{ru.HEALTH}: {health} \n{ru.FORCE}: {force}')
            else:
                print(f'{ru.GRANNY_GOD}')
        else:
            print(f'{ru.CLOSE_DOOR}')
    return force





names = []
for i in range(4):
    name = input(f'{ru.NAME} {i+1}->')
    names.append(name)

print(ru.INITIAL_INFO)
print(f'{ru.RESOURCES}:\n{ru.HEALTH} 3\n{ru.FORCE} 5')

act1 = []
for i in names:
    print(f'{i}, {ru.CHOOSE}:\n1.{ru.DOWN}\n2.{ru.GO}\n3.{ru.ENTER}')
    action1 = int(input(f'{ru.ACT}->'))
    act1.append(action1)

for i in act1:
    if i == 1:
        if floor_1() >= random.Random(5):
            print('Вы победили')
        else:
            print('лох')
    else:
        if floor2() >= random.randint(0, 5):
            print(ru.CONTINGENCY)
            print('Вы победили')
        else:
            print(ru.CONTINGENCY)
            print('лох')
