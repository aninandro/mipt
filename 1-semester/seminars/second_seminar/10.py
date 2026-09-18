with open("input11.txt", "r") as f:
    s = "".join("".join(f.readlines()).splitlines()).strip().lower().split()
    arr = []
    vowels = {
            "я" : "а",
            "ю" : "у",
            "ё" : "о",
            "е" : "э",
            "э" : "э",
            "о" : "о",
            "у" : "у",
            "а" : "а",
            "и" : "и"
            }
    for word in s:
        new_word = ""
        for letter in range(len(word)):
            new_word += word[letter]
            if new_word[-1] in "аяуюоёеэиы" and letter != 0 and word[letter-1] not in "аяуюоёеэиы":
                new_word += "с" + vowels[new_word[-1]]
                while letter < len(word) and word[letter] in "аяуюоёеэиы":
                    letter += 1


        arr.append(new_word)
    print(" ".join(arr))




   
