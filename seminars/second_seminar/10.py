with open("input10.txt", "r") as f:
    s = "".join("".join(f.readlines()).splitlines()).strip().lower().split()
    arr = []
    for word in s:
        for letter in range(len(word)):
            l = word[letter]
            print(l)
            if l in "аяуюоёеэиы":
                word = word[:letter+1] + f"с{l}"
                print(word)
        arr.append(word)
    print(arr)




   
