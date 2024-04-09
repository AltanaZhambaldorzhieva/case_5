# Case_3
# Developers: Zhambaldorzhieva A., Ryaguzova D., Zaitseva D.
#
import ru_local as ru
import random

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

def floor2():
    health = 3
    force = 5
    print(f'{ru.CHOOSE}:\n1.{ru.GO}\n2.{ru.ENTER}')
    act = int(input(f'{ru.ACT}->'))
    if act == 1:
        if def random_granny() == 2:
            print(f'{ru.OH_OH}')
            health -= 1
            force -= 2
        print(f'{ru.CHOOSE}:\n1.{ru.GO_TO_ROOM_1}\n2.{ru.GO_TO_ROOM_2}')
        act1 = int(input(f'{ru.ACT}->'))
        if act1 == 1:
            print(f'{ru.CHOOSE}:\n1.{ru.OPEN_WARDROBE}\n2.{ru.OPEN_FRIDGE}')
            act2 = int(input(f'{ru.ACT}->'))
            if act2 == 1:
                print(f'{ru.EMPTY}')
            else:
                print(f'{ru.SPRAY}')
        else:
            print(f'{ru.EMPTY})
        print(f'{ru.CHOOSE}:\n1.{ru.GO}\n2.{ru.GO_TO_ROOM_1})
        act3 = int(input(f'{ru.ACT}->'))
        if act3 == 1:
            if def random_granny() == 2:
            print(f'{ru.OH_OH}')
            health -= 1
            force -= 2
            print(f'{ru.CHOOSE}:\n1.{ru.GO}\n2.{ru.GO_TO_ROOM_3}')
            act4 = int(input(f'{ru.ACT}->'))
            if act4 == 1:
                if def random_granny() == 2:
                    print(f'{ru.OH_OH}')
                    health -= 1
                    force -= 2
            else:
                print(f'{ru.CHOOSE}:\n1.{ru.OPEN_WARDROBE}\n2.{ru.OPEN_BAG}')
                act5 = int(input(f'{ru.ACT}->'))
                if act5 == 1:
                    print(f'{ru.MEDICINE}')
                    health += 1
                    if health > 3:
                        health = 3
                else:
                    print(f'{ru.EMPTY}')
        else:
            print(f'{ru.CHOOSE}:\n1.{ru.OPEN_WARDROBE}\n2.{ru.OPEN_FRIDGE}')
            act2 = int(input(f'{ru.ACT}->'))
            if act2 == 1:
                print(f'{ru.EMPTY}')
            else:
                print(f'{ru.SPRAY}')
    else:
        print(f'{ru.CHOOSE}:\n1.{ru.OPEN_WARDROBE}\n2.{ru.OPEN_BAG}')
        act5 = int(input(f'{ru.ACT}->'))
        if act5 == 1:
            print(f'{ru.MEDICINE}')
            health += 1
            if health > 3:
                health = 3
    return health, force


def random_granny():
    rand_granny = random.choice([1, 2])
    return rand_granny
