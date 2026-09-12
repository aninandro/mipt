G = int(input("Enter number of groups N: "))
S = str(input("Enter string: "))
result = ""

if len(S) % G != 0:
    print("Error, string length not a multiple of N")
else:
    for i in range(0, len(S), G):
        substring = S[i:i+G][::-1]
        result += substring
    print(result)


        
