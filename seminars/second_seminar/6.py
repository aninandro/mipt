arr = []
print("Enter elements (type 'stop' to stop input): \n")
n = input()

while n != "stop":
    arr.append(n)
    n = input()
if len(arr) == 0:
    print("Error, list must be filled")
else:
    flag = False
    for i in arr:
        if arr.count(i) == 1:
            print(i, end = " ")
            flag = True
    if flag == False:
        print("No unique elements", end = "")
print("\n")
