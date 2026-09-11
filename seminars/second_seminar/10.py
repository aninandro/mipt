with open("input10.txt", "r") as f:
    s = "".join("".join(f.readlines()).splitlines()).strip().lower().split()
    arr = []
    for word in s:
        new_word = ""
        for letter in range(len(word)):
            new_word += word[letter]
            if new_word[-1] in "аяуюоёеэиы":
                new_word += "с" + new_word[-1]
                while letter < len(word) and word[letter] in "аяуюоёеэиы":
                    letter += 1


        arr.append(new_word)
    print(" ".join(arr))




   
