cards = []
n = int(input("Enter number of cards: "))
if n > 54:
    print("Error, n exceeded 54")
else:
    cards = [int(input(f"Enter {x+1}th card value: ")) for x in range(n-1)]

for i in range(1, n + 1):
    if i not in cards:
        print(f"Missing card is: {i}")
        break
