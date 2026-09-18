arr = []
print("Enter elements (type 'stop' to stop input): \n")
n = input()

while n != "stop":
    arr.append(n)
    n = input()
if len(arr) == 0:
    print("Error, list must be filled")
else:
    arr.insert(0,arr[-1])
    arr.pop()

    print(arr)
