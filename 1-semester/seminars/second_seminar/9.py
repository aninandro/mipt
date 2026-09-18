with open('input.txt', 'r') as f:
    s = "".join("".join(f.readlines()).splitlines())
    print(s)
    s = s.replace("?", ".").replace("!", ".")
    while ".." in s:
        s = s.replace("..", ".")
    s = s.strip()
    result = len(s.split(".")[:-1])
    print(result)
