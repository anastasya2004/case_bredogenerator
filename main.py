import random

text = 'Метель в поле страшная. Колкий снег бьёт и колет всё живое. Но в лесу снег рыхлый и от собаки даже проваливается. Сквозь метель Жулька увидела летящую птичку и со всех ног бросилась за ней по снегу. Птичка плавно порхала, поднималась вверх и вертелась в волнах ветра. Она догнала, схватила, но это была не птичка, а старый сухой дубовый лист. Но ничего! Вот другой летит, и собака уже бежит за ним'
#text = input()

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
    text_delusion = [word]
    for x in range(numbers_words - 1):
        next_word = random.choice(dict_word[word])
        text_delusion.append(next_word)
        word = next_word
    return ' '.join(text_delusion)

