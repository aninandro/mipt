f = open("input.txt","r")
arr = f.read().splitlines()
numbers = arr[0]
operation = arr[1]

f.close()

a = numbers.split(" ")
s = int(a[0])

if operation == "+":
    for i in range(1,len(a)):
        s += int(a[i])
elif operation == "-":
    for i in range(1, len(a)):
        s -= int(a[i])
elif operation == "*":
    for i in range(1, len(a)):
        s *= int(a[i])

file = open("output.txt", "w")
file.write(str(s) + "\n")
file.close()
    
