arr = [1,1,2,2]
most_frequent = arr[0]
frequence = 0
for i in arr:
    if arr.count(i) > frequence:
        most_frequent = i
        frequence = arr.count(i)

print(most_frequent)
