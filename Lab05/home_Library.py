class home_Library:
    library = []
    name = "NONAME"
    author = "NONAME"
    year = "UNKNOWN"

    def addBook(self, nameBook = "NONAME", authorBook = "NONAME", yearBook = "UNKNOWN"):
        name = nameBook
        author = authorBook
        year = yearBook
        self.library += [name, author, year]

    def deleteBook(self):
        self.library.clear()
        
    def searchAuthor(self, author):
        for data in self.library:
            if(self.library[1] == author):
                print("Є такий автор")
                break
            else:
                print("Такого автора у бібліотеці не має")
                break

    def searchYear(self, year):
        for data in self.library:
            if(self.library[2] == year):
                print("Існує книга такого року")
                break
            else:
                print("Книги такого року у бібліотеці не має")
                break

    
        




