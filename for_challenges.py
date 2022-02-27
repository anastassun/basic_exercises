# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

from operator import index
from re import X


names = ['Оля', 'Петя', 'Вася', 'Маша']
def main():
    for x in names: 
        print(x)
    #print(*names, sep='\n')
if __name__ == "__main__":
    main()



# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

names = ['Оля', 'Петя', 'Вася', 'Маша']
def main():
    for x in names: 
        print(f'{x}:{len(x)}')
    #print(*names, sep='\n')
if __name__ == "__main__":
    main()


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
def main():
    for x in names:
        if is_male.get(x) == True:
            print(x + " - male ")
        else:
            print(x + " - female ")

        #print(f'{x}:{False,True }')
    #print(*names, sep='\n')
if __name__ == "__main__":
    main()


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]
def main():
    print(f" Всего { len(groups)} группы")
for index, group in enumerate(groups): 
    print(f" Группа {index} : { len(groups)} ученика")
    #print(*names, sep='\n')
if __name__ == "__main__":
    main()


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]
def main():
    for index, group in enumerate(groups): 
        print(f'Группа {index}:', end=' ')
        print(','.join(group))
if __name__ == "__main__":
    main()