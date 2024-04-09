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
    random_granny = random.choice([0, 1])
    if random_granny == 0:
        print('')








