

def prime(n):
    p = 2
    arr = []
    while n > 1:
        if n % p == 0:
            arr.append(p)
            n //= p
        else:
            p += 1
    return arr


print(prime(60))
