

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n-2)


def main():
    n = int(input("Enter N: "))
    x = fibonacci(n)
    print(f"{n}-th fibonacci number is: {x}.")
    return 0

main()
