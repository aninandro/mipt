

def triangle(cnt, current, symb):
    if current > cnt:
        return

    print(current * symb)
    triangle(cnt, current + 1, symb)
    
    if current < cnt:
        print(current * symb)

def main():
    stdin = input("Enter size and symb: ")
    stdin = stdin.split()
    size = int(stdin[0])
    symb = stdin[1]
    cnt = (size + 1) // 2

    triangle(cnt, 1, symb)
    return 0

main()
