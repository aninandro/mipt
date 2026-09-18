

def prime(n):
    d = 2
    arr = []
    while n > 1:
        if n % d == 0:
            arr.append(d)
            n //= d
        else:
            d += 1
    return arr

def main():
    number = int(input("Enter number: "))
    x = prime(number)
    print(f"Prime factors of {number}: {x}.")

main()
