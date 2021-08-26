import home_Library
import Student
import str_Nasledovanie
import deck_of_Cards
import Vocabulary
import Transport

#Task1
#print("Task1:\n")
#book = home_Library.home_Library()
#book.addBook("Місто", "Підмогильний", 1996)
#print(book.library)
#book.searchAuthor("Підмогильний")
#book.searchYear(1996)


#Task2
#print("Task2:\n")
#Danilo = Student.Student("Данило")
#Danilo.TryLab()
#Danilo.TryIndivTask()
#Danilo.Result()


#Task3
#print("Task3:\n")
#example1 = str_Nasledovanie.str_Nasledovanie(b'')
#example2 = str_Nasledovanie.str_Nasledovanie(b'')
#arg = example1.if_palidrom("Пилип")
#print("Cлово паліндром - ", arg)
#print("Повторення - ")
#example2.repeats("hahnuhah")


#Task4
#print("Task4:\n")
#Coloda = deck_of_Cards.Stack()
#print("Уся колода:\n")
#Coloda.showall()

#print("\nКарта у 9 позиції\n")
#Coloda.findbyindex(9)

#print("\nОдна випадкова карта: \n")
#Coloda.getonecard()

#print("\nШість випадкових карт:\n")
#Coloda.getsixcards()

#print("\nПеремішування колоди: \n")
#Coloda.mixing_the_Deck()


#Task5
#print("Task5:\n")
#word = Vocabulary.Vocabulary()
#print("Усі слова словника: ", word.showVocabulary())
#print(word.translate())


#Task6
#print("Task6:\n")
Lancer = Transport.Car()
Lancer.setval(15000.0)
Lancer.setspeed(300)
Lancer.setyear(2004)
Lancer.setcoord("12:04:255")
Lancer.showCar()