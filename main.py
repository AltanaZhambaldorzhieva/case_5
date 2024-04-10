# Case_3
# Developers: Zhambaldorzhieva A., Ryaguzova D., Zaitseva D.
#
import ru_local as ru
import random


def random_granny():
    """
        The function returns random generation of granny location floor
    """
    rand_granny = random.choice([1, 2])
    return rand_granny


def floor_1(j):
    """
        The function returns the amount of remaining force on the first floor
    """
    health = 3
    force = 5
    print(f'{j}, {ru.CHOOSE}:\n1.{ru.KITCHEN}\n2.{ru.GO}\n3.{ru.EXIT}')
    act_1 = int(input(f'{ru.ACT}->'))
    if act_1 == 1:
        print(f'{ru.KITCHEN_PL} {ru.CHOOSE}:\n1.{ru.OPEN_FRIDGE}\n2.{ru.OPEN_WARDROBE}')
        act_2 = int(input(f'{ru.ACT}->'))
        if act_2 == 1:
            print(f'{ru.EAT}')
            if force < 5:
                force += 1
                print(f'{ru.FORCE}: {force}')
            else:
                force = 5
                print(f'{ru.FORCE}: {force}')
        else:
            print(f'{ru.EMPTY}\n{ru.RETURN}\n1.{ru.GO}\n2.{ru.EXIT}')
            act_3 = int(input(f'{ru.ACT}->'))
            if act_3 == 1:
                if random_granny() == 1:
                    health -= 1
                    force -= 2
                    if health == 0:
                        print(f'{ru.DEATH}')
                        exit()
                    else:
                        print(f'{ru.GRANNY_BAD}\n{ru.RESOURCES}'
                              f'\n{ru.HEALTH}: {health} \n{ru.FORCE}: {force}')
                else:
                    print(f'{ru.GRANNY_GOD}\n{ru.RESOURCES}'
                          f'\n{ru.HEALTH}: {health} \n{ru.FORCE}: {force}')
            else:
                print(f'{ru.CLOSE_DOOR}\n{ru.RETURN}\n1.{ru.KITCHEN}\n2.{ru.GO}')
                act_4 = int(input(f'{ru.ACT}->'))
                if act_4 == 1:
                    print(f'{ru.BEEN}')
                else:
                    if random_granny() == 1:
                        health -= 1
                        force -= 2
                        if health == 0:
                            print(f'{ru.DEATH}')
                            exit()
                        else:
                            print(f'{ru.GRANNY_BAD}\n{ru.RESOURCES}'
                                  f'\n{ru.HEALTH}: {health} \n{ru.FORCE}: {force}')
                    else:
                        print(f'{ru.GRANNY_GOD}\n{ru.RESOURCES}'
                              f'\n{ru.HEALTH}: {health} \n{ru.FORCE}: {force}')
    elif act_1 == 2:
        if random_granny() == 1:
            health -= 1
            force -= 2
            if health == 0:
                print(f'{ru.DEATH}')
                exit()
            else:
                print(f'{ru.GRANNY_BAD}\n{ru.RESOURCES}'
                      f'\n{ru.HEALTH}: {health} \n{ru.FORCE}: {force}')
        else:
            print(f'{ru.GRANNY_GOD}\n{ru.RESOURCES}'
                  f'\n{ru.HEALTH}: {health} \n{ru.FORCE}: {force}')
    else:
        print(f'{ru.CLOSE_DOOR}')
    return force


def floor_2(n):
    """
        The function returns the amount of remaining force on the second floor.
    """
    health = 3
    force = 5
    spray = 0
    print(f'{n}, {ru.CHOOSE}:\n1.{ru.GO}\n2.{ru.ENTER}')
    act = int(input(f'{ru.ACT}->'))
    if act == 1:
        if random_granny() == 2:
            health -= 1
            force -= 2
            if health == 0:
                print(f'{ru.DEATH}')
                exit()
            else:
                print(f'{ru.GRANNY_BAD}\n{ru.RESOURCES}'
                        f'\n{ru.HEALTH}: {health} \n{ru.FORCE}: {force}')
        print(f'{n}, {ru.CHOOSE}:\n1.{ru.GO_TO_ROOM_1}\n2.{ru.GO_TO_ROOM_2}')
        act_1 = int(input(f'{ru.ACT}->'))
        if act_1 == 1:
            print(f'{n}, {ru.CHOOSE}:\n1.{ru.OPEN_WARDROBE}\n2.{ru.OPEN_FRIDGE}')
            act_2 = int(input(f'{ru.ACT}->'))
            if act_2 == 1:
                print(ru.EMPTY)
            else:
                print(ru.SPRAY)
                spray += 1
        else:
            print(ru.EMPTY)
        print(f'{n}, {ru.CHOOSE}:\n1.{ru.GO}\n2.{ru.GO_TO_ROOM_1}')
        act_3 = int(input(f'{ru.ACT}->'))
        if act_3 == 1:
            if random_granny() == 2:
                health -= 1
                force -= 2
                if health == 0:
                    print(f'{ru.DEATH}')
                    exit()
                else:
                    print(f'{ru.GRANNY_BAD}\n{ru.RESOURCES}'
                            f'\n{ru.HEALTH}: {health} \n{ru.FORCE}: {force}')
            print(f'{n}, {ru.CHOOSE}:\n1.{ru.GO}\n2.{ru.GO_TO_ROOM_3}')
            act_4 = int(input(f'{ru.ACT}->'))
            if act_4 == 1:
                if random_granny() == 2:
                    health -= 1
                    force -= 2
                    if health == 0:
                        print(f'{ru.DEATH}')
                        exit()
                    else:
                        print(f'{ru.GRANNY_BAD}\n{ru.RESOURCES}'
                                f'\n{ru.HEALTH}: {health} \n{ru.FORCE}: {force}')
            else:
                print(f'{n}, {ru.CHOOSE}:\n1.{ru.OPEN_WARDROBE}\n2.{ru.OPEN_BAG}')
                act_5 = int(input(f'{ru.ACT}->'))
                if act_5 == 1:
                    print(f'{ru.MEDICINE}')
                    health += 1
                    if health > 3:
                        health = 3
                else:
                    print(f'{ru.EMPTY}')
        else:
            print(f'{n}, {ru.CHOOSE}:\n1.{ru.OPEN_WARDROBE}\n2.{ru.OPEN_FRIDGE}')
            act_2 = int(input(f'{ru.ACT}->'))
            if act_2 == 1:
                print(f'{ru.EMPTY}')
            else:
                print(f'{ru.SPRAY}')
                spray += 1
    else:
        print(f'{n}, {ru.CHOOSE}:\n1.{ru.OPEN_WARDROBE}\n2.{ru.OPEN_BAG}')
        act_5 = int(input(f'{ru.ACT}->'))
        if act_5 == 1:
            print(f'{ru.MEDICINE}')
            health += 1
            if health > 3:
                health = 3
    return force


names = []
for i in range(4):
    name = input(f'{ru.NAME} {i+1}->')
    names.append(name)


print(ru.INITIAL_INFO)
print(f'{ru.RESOURCES}: {ru.HEALTH} 3 {ru.FORCE} 5')

act1 = []
for i in names:
    print(f'{i}, {ru.CHOOSE}:\n1.{ru.DOWN1}\n2.{ru.DOWN2}')
    action1 = int(input(f'{ru.ACT}->'))
    act1.append(action1)

for name in names:
    if act1[names.index(name)] == 1:
        n1 = random.randint(1, 5)
        if floor_1() >= n1:
            print(ru.CONTINGENCY)
            print(ru.FIGHT)
            print(f'{ru.GRANNY_FORCE}: {n1}\n{ru.WINNER_FORCE}')
            print(ru.WINNER)
        else:
            print(ru.CONTINGENCY)
            print(ru.FIGHT)
            print(f'{ru.GRANNY_FORCE}: {n1}\n{ru.LOSER_FORCE}')
            print(ru.LOSER)
    else:
        n2 = random.randint(1, 5)
        if floor_2() >= n2:
            print(ru.CONTINGENCY)
            print(ru.FIGHT)
            print(f'{ru.GRANNY_FORCE}: {n2}\n{ru.WINNER_FORCE}')
            print(ru.WINNER)
        else:
            print(ru.CONTINGENCY)
            print(ru.FIGHT)
            print(f'{ru.GRANNY_FORCE}: {n2}\n{ru.LOSER_FORCE}')
            print(ru.LOSER)
