import os
import os.path

def read_File1():#читання 1 файлу
    f1 = open('group1.txt', encoding='utf-8')
    print(f1.read())
    f1.close()

def read_File2():#читання 2 файлу
    f2 = open('group2.txt', encoding='utf-8')
    print(f2.read())
    f2.close()

def write_File1():#запис в 1 файл
    f1 = open('group1.txt', 'w' ,encoding='utf-8')
    f1.write("test")
    f1.close()

def write_File2():#запис в 2 файл
    f2 = open('group2.txt', 'w' ,encoding='utf-8')
    f2.write("test")
    f2.close()

def file1_app():#дозапис в 1 файл
    f1 = open('group1.txt', 'a' ,encoding='utf-8')
    f1.write("\nNONAME - 60")
    print("Відбувся дозапис!")
    f1.close()

def file2_app():#дозапис в 2 файл
    f2 = open('group2.txt', 'a' ,encoding='utf-8')
    f2.write("\nNONAME - 60")
    print("Відбувся дозапис!")
    f2.close()


print("=====================================================================")
read_File1()
print("=====================================================================")
read_File2()
print("=====================================================================")
file2_app()
print("=====================================================================")
read_File2()
print("=====================================================================")

# Пошук файлу в каталозі

filedir = "groups2.txt"
cur_dir = os.getcwd()

file_list = os.listdir(cur_dir)
parent_dir = os.path.dirname(cur_dir)
print("Файл в: ", cur_dir)
        
# Пошук даних у файлі
word = 'Андрій'
f2 = open('group2.txt', encoding='utf-8') 
text = f2.read()
counter = text.count(word)
print("Кількість повторень слова Андрій у файлі:",counter)

# Сортування за балами
f2 = open('group2.txt', encoding='utf-8') 
with open('group2.txt', 'r' ,encoding='utf-8') as f:
    l = f2.readlines()
    l.sort(key=lambda line: int(line.split('-') [1]))
    print(l)
f2.close()