

def triangle(size, current, symb):
    maximum = (size + 1) // 2
    if current > maximum:
        return
    print(current * symb)
    triangle(size, current + 1, symb)
    if current < maximum or (current == maximum and size % 2 == 0):
        print(current * symb)

def main():
    user_input = input("Enter size and symb: ")
    user_input = user_input.split()
    size = int(user_input[0])
    symb = user_input[1]

    triangle(size, 1, symb)

main()
