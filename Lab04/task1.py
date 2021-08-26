import random

first_word = ["Я ","Ти ","Він ","Вона ","Вони ","Ми ","Андрій ","Оксана "]
second_word = ["грає ","працює ","ходить ","дивиться ","займається ","починає "]
third_word = ["у копм'ютер","на заводі","у школу","кіно","спортом","танцювати","на гітарі","комедію","сумувати"]

print(random.choice(first_word) + random.choice(second_word) + random.choice(third_word))