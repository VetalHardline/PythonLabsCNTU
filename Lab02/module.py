import random
import numpy

array = []
for elem in range(10):
    elem = random.randint(0, 15)
    array.append(elem)
print(array)

def quickSort():
    array.sort()
    print(array)

def search_value_in_array():
    i = int(input("Введіть значення: "))
    if i in array:
        print("Значення ", i, "є в масиві")
    else:
        print("Значення ", i, "не має в масиві")

def search_poslidovnist_in_array():
    value = int(input("Уведіть кількість елементів послідовності: "))
    values = []
    for elem in range(value):
        values.append(int(input("Уведіть число: ")))
    print(values)
    print("Статус операції: ",all(elem in array for elem in values))

def search_min_five():
    array.sort()
    print("Перші п'ять мінімальні елементи:")
    print(array[:5])

def search_max_five():
    array.sort()
    print("Перші п'ять максимальні елементи:")
    print(array[5:10])

def arithmetic_mean():
    print(("Середнє арифметичне:"),numpy.mean(array))

def without_repeats():
    print("Список без повторень: ",list(set(array)))