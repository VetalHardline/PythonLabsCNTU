print("This program determines whether n is a prime number")
n = int(input("Уведіть n: "))

if n < 2:
    print("Число повинно бути 2 або більше")
    quit()

for elem in range(2, n):
    if n % elem == 0:
        print("Число n складене")
        quit()
print("Число n просте")
