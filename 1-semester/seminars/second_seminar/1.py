cards = []
n = int(input("Enter number of cards n: "))
if n > 54:
    print("Error, n exceeded 54")
elif n < 1:
    print("Error, n must be natural")
else:
    x = 0
    while x < n - 1:
        value = int(input(f"Enter {x+1}th card value: "))
        if value in cards:
            print("Error, value already entered\n")
        elif value < 1:
            print("Error, value must be positive\n")
        elif value > n:
            print("Error, value must not exceed the number of cards\n")
        else:
            cards.append(value)
            x += 1

    #cards = [int(input(f"Enter {x+1}th card value: ")) for x in range(n-1)]

    for i in range(1, n + 1):
        if i not in cards:
            print(f"\nMissing card is: {i}")
            break
