#Makeeva Angelina 58%
#Osokina Anastasya 72%
#Kareva Alena 60%
import random
import string

with open('text.txt', 'r+') as file:
    text = file.read()


    lst_word = text.split()

    pairs = []
    for i in range(len(lst_word) - 1):
        pairs.append([lst_word[i], lst_word[i+1]])

    dict_word = {}
    for i in range(len(pairs)):
        w1 = pairs[i][0]
        w2 = pairs[i][1]
        if w1 in dict_word.keys():
            dict_word[w1].append(w2)
        else:
            dict_word[w1] = [w2]


    def create_delusion(dict_word, first_word, numbers_words):
        word = first_word
        text_delusion = [word.capitalize()]
        for x in range(numbers_words - 1):
            next_word = random.choice(dict_word[word])
            text_delusion.append(next_word)
            word = next_word.rstrip(string.punctuation)
        return ' '.join(text_delusion)

    first_word = random.choice(lst_word)
    numbers_words = int(input("Выберите количество слов бреда: "))
    print(create_delusion(dict_word, first_word, numbers_words))
    file.seek(0)
    file.write(create_delusion(dict_word, first_word, numbers_words))
    file.truncate()
