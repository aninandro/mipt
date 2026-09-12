arr = []
print("Enter elements (type 'stop' to stop input): \n")
n = input()

while n != "stop":
    arr.append(n)
    n = input()
if len(arr) == 0:
    print("Error, list must be filled")
else:
    most_frequent = arr[0]

    frequence = 0
    for i in arr:
        if arr.count(i) > frequence:
            most_frequent = i
            frequence = arr.count(i)

    print(most_frequent)
