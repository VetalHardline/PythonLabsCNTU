import random
from functools import reduce
N = int(input("Уведіть N: "))
if N < 2:
    print("Для того, щоб працювати з масивом, число N має бути 2 або більше")
    quit()

array = []
for elem in range(0,N):
    i = random.randint(0,10)
    array.append(i)
print("Масив: ", array)
print("Мінімальний додатній елемент: ", min(array))
pairedElements = [n for n in array if not n % 2]
print("Сума парних елементів масиву: ", reduce(lambda x,y: x + y, pairedElements))
array.reverse()
print("Масив у зворотньому порядку: ", array)



