class Vocabulary:
    def __init__(self, word = "Unknown"):
        self.EnglishVocabulary = {
            "love" : ["любовь", "cтрасть", "привязанность"], 
            "point" : ["точка", "балл", "пункт"],
            "beach" : ["пляж", "берег моря", "отмель"],
            "test" : ["контрольная робота", "тест", "проверка"]}
        self.word = word

    def showVocabulary(self):
        return self.EnglishVocabulary.keys()

    def translate(self):
        self.word = input("Введіть слово, яке хочете перевести: ")
        if self.word in self.EnglishVocabulary.keys():
            return self.EnglishVocabulary.get(self.word)
        else:
            print("Такого слова в словнику не має")
