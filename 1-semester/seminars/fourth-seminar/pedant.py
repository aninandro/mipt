from pathlib import Path
import string


with Path("fourth-seminar/python_license.txt").open() as file:
    text = " ".join(file.read().splitlines())
    for sign in string.punctuation:
        text = text.replace(sign, " ")

    arr = text.split()

    word_counter = {}
    for w in arr:
        word = w.lower()
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1


    for _ in range(10):
        if len(word_counter.keys()) == 0:
            break
        max_key = max(word_counter, key = word_counter.get)
        print(max_key, word_counter[max_key])
        del word_counter[max_key]
