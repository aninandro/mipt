

# fibonacci function
def fibonacci(n):
    numbers = [0] * n
    numbers[1] = 1

    for i in range(2, n):
        numbers[i] = numbers[i-1] + numbers[i-2]

    return numbers[-1]


# main
def main():
    n = int(input("Enter N: "))
    x = fibonacci(n)
    print(f"{n}-th fibonacci number is {x}.")
    return 0


main()
