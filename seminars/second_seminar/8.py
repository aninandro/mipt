N = int(input("Enter number N: "))
numbers = str(input("Enter elements (sep - space):\n"))
numbers = numbers.split()
numbers = list(map(int, numbers))

for i in range(len(numbers)):
    elem = numbers[i]
    k = 0
    for j in range(len(numbers)):
        if numbers[j] < elem:
            k += 1
        if k > (N // 2):
            break
    if k == (N // 2):
        print(elem)
        break
