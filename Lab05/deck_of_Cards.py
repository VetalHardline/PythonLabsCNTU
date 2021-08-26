import random

class deck_of_Cards:

    def __init__(self):
        self.mast = random.choice(["chirva", "pika", "chresta", "bubna"])
        self.num = random.choice([6, 7, 8, 9, 10, "V", "D", "K", "A"])

    def show(self):
        print("Mast: " + self.mast + "\n" + "Num: " + str(self.num))

class Stack:

    def __init__(self):
        self.stack = list()
        for i in range(35):
            random_card = deck_of_Cards()
            if random_card not in self.stack:
                self.stack.append(random_card)

    def findbyindex(self, index):
        if 0<=index<=35:
            print("Карта з колоди за індексом: " + str(index))
            self.stack[index].show()
        else:
            print("число має бути від 0 до 35")

    def showall(self):
        for index in range(35):
            self.stack[index].show()

    def getonecard(self):
            random.choice(self.stack).show()

    def getsixcards(self):
        for i in range(6):
            random.choice(self.stack).show()

    def mixing_the_Deck(self):
        new = random.sample(self.stack,len(self.stack))
        for elem in new:
            print(elem.show())