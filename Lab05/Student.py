class Student:
    amountAttempts = 0
    amountAttemptTask = 0
    dataLab = 0
    datIndivTask = 0

    def __init__(self, name = "NONAME"):
        self.name = name
        self.studentVocabulary = {
            "максимально можлива кількість балів за здачу індивідуального творчого завдання" : 10,
            "максимально можлива кількість балів за здачу однієї лабораторної роботи" : 10,
            "кількість лабораторних робіт в курсі" : 7,
            "частка балів від максимуму, яку необхідно набрати для отримання екзамену автоматом" : 60}

    def TryLab(self):
        amountAttempts = int(input("Уведіть скільки разів ви намагалися здати лабораторну роботу: "))
        if(amountAttempts == 1):
            self.dataLab = int(self.studentVocabulary.get("максимально можлива кількість балів за здачу однієї лабораторної роботи"))
            print("Ваш бал: ", self.dataLab)
        if(amountAttempts == 2):
            self.dataLab = int(self.studentVocabulary.get("максимально можлива кількість балів за здачу однієї лабораторної роботи") - 1)
            print("Ваш бал: ", self.dataLab)
        if(amountAttempts == 3):
            self.dataLab = int(self.studentVocabulary.get("максимально можлива кількість балів за здачу однієї лабораторної роботи") - 2)
            print("Ваш бал: ", self.dataLab)
        if(amountAttempts > 3):
            self.dataLab = int(self.studentVocabulary.get("максимально можлива кількість балів за здачу однієї лабораторної роботи") - 5)
            print("Ваш бал: ", self.dataLab)

    def TryIndivTask(self):
        amountAttemptTask = int(input("Уведіть скільки разів ви намагалися здати індивідуальне завдання: "))
        if(amountAttemptTask == 1):
            self.datIndivTask = int(self.studentVocabulary.get("максимально можлива кількість балів за здачу індивідуального творчого завдання"))
            print("Ваш бал: ", self.datIndivTask)
        if(amountAttemptTask == 2):
            self.datIndivTask = int(self.studentVocabulary.get("максимально можлива кількість балів за здачу індивідуального творчого завдання") - 1)
            print("Ваш бал: ", self.datIndivTask)
        if(amountAttemptTask == 3):
            self.datIndivTask = int(self.studentVocabulary.get("максимально можлива кількість балів за здачу індивідуального творчого завдання") - 2)
            print("Ваш бал: ", self.datIndivTask)
        if(amountAttemptTask > 3):
            self.datIndivTask = int(self.studentVocabulary.get("максимально можлива кількість балів за здачу індивідуального творчого завдання") - 5)
            print("Ваш бал: ", self.datIndivTask)
    
    def Result(self):
        result = ((self.dataLab*7 + self.datIndivTask))
        score = int(self.studentVocabulary.get("частка балів від максимуму, яку необхідно набрати для отримання екзамену автоматом"))
        if result == score or result > score:
            print(result)
            print(True)
        else:
            print("Ваш результат: ", result)
            print(False)