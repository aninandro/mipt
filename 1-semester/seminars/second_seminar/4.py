arr = []
print("Enter elements (type 'stop' to stop input): \n")
n = input()

while n != "stop":
    arr.append(n)
    n = input()
if len(arr) == 0:
    print("Error, list must be filled")
else:
    for i in range(0, len(arr) - (len(arr) % 2), 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    print(arr)
