N = int(input("Enter number N: "))
numbers = [int(input("Enter element: ")) for _ in range(N)]

for i in range(len(numbers)):
    elem = numbers[i]
    k = 0
    for j in range(len(numbers)):
        if numbers[i] < elem:
            k += 1
        if k > (N // 2):
            break
    if k == (N//2):
        print(elem)
        break
