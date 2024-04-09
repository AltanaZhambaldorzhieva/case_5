# Case_3
# Developers: Zhambaldorzhieva A., Ryaguzova D., Zaitseva D.
#
import ru_local as ru

player1 = input(f'{ru.NAME} 1->')
player2 = input(f'{ru.NAME} 2->')
player3 = input(f'{ru.NAME} 3->')
player4 = input(f'{ru.NAME} 4->')

print(ru.INITIAL_INFO)
print(f'{ru.RESOURCES}:\n{ru.HEALTH} 3\n{ru.FORCE} 5')

print(f'{player1}, {ru.CHOOSE}:\n1.{ru.DOWN}\n2.{ru.GO}\n3.{ru.ENTER}')
act1 = int(input(f'{ru.ACT}->'))
print(f'{player2}, {ru.CHOOSE}:\n1.{ru.DOWN}\n2.{ru.GO}\n3.{ru.ENTER}')
act2 = int(input(f'{ru.ACT}->'))
print(f'{player3}, {ru.CHOOSE}:\n1.{ru.DOWN}\n2.{ru.GO}\n3.{ru.ENTER}')
act3 = int(input(f'{ru.ACT}->'))
print(f'{player4}, {ru.CHOOSE}:\n1.{ru.DOWN}\n2.{ru.GO}\n3.{ru.ENTER}')
act4 = int(input(f'{ru.ACT}->'))
