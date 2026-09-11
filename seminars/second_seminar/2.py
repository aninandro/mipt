N = int(input("Enter number of groups N: "))
S = str(input("Enter string: "))
result = ""

if len(S) % N != 0:
    print("Error, string length not a multiple of N")
else:
    for i in range(0, len(S), N):
        substring = S[i:i+N][::-1]
        result += substring
    print(result)


        
