# Case_3
# Developers: Zhambaldorzhieva A., Ryaguzova D., Zaitseva D.
#
import ru_local as ru
import random

names = []
for i in range(4):
    name = input(f'{ru.NAME} {i+1}->')
    names.append(name)

health = 3
force = 5
print(ru.INITIAL_INFO)
print(f'{ru.RESOURCES}:\n{ru.HEALTH} {health}\n{ru.FORCE} {force}')

act1 = []
for i in names:
    print(f'{i}, {ru.CHOOSE}:\n1.{ru.DOWN}\n2.{ru.GO}\n3.{ru.ENTER}')
    action1 = int(input(f'{ru.ACT}->'))
    act1.append(action1)


def random_granny():
    rand_granny = random.choice([1, 2])
    return rand_granny

def room_3():
    print(f'{ru.CHOOSE}:\n1.{ru.OPEN_WARDROBE}\n2.{ru.OPEN_BAG}')
    act = int(input(f'{ru.ACT}->'))
    if act == 1:
        print(f'{ru.MEDICINE}')
        helth += 1
        if helth > 3:
            helth = 3
    else:
        print(f'{ru.EMPTY}')








