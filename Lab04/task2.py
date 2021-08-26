fr = open("text.txt", "r", encoding='utf8')

text = str()
words = dict()
symbols_without_space = 0
spaces = 0
unique_words = 0

for line in fr:
    text += line

fr.close()

for symbol in text:
    if symbol == ' ':
       spaces += 1
    else:
        symbols_without_space += 1

print("Кількість символів з пробілами: " + str(symbols_without_space + spaces))
print("Кількість символів без пробілів: " + str(symbols_without_space))

for sent in text.split("\n\t"):
    for word in sent.split(" "):
        word = word.lower()
        for symbol in word:
            if not symbol.isalpha():
                word = word.replace(symbol,'')
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

print(words)

for elem in words:
    if words[elem] == 1:
        unique_words += 1

print("Кількість унікальних слів: " + str(unique_words))