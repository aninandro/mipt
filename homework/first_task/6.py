def conversion(n, base):
    s = ""
    while n > 0:
        s = str(n % base) + s
        n //= base
    return s


f = open("input6.txt","r")
arr = f.read().splitlines()
numbers = arr[0]
operation = arr[1]
base = int(arr[2])

f.close()

a = numbers.split(" ")
s = int(a[0], base)

if operation == "+":
    for i in range(1,len(a)):
        s += int(a[i], base)
elif operation == "-":
    for i in range(1, len(a)):
        s -= int(a[i], base)
elif operation == "*":
    for i in range(1, len(a)):
        s *= int(a[i], base)

file = open("output6.txt", "w")
file.write(conversion(s, base) + "\n")
file.close()
    
