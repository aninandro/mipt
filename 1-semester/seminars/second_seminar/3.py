def check_mirror(string):
    mirror_letters = {
        "A" : "A", "H" : "H", "I" : "I", "M" : "M", "O" : "O", "T" : "T",
        "U" : "U", "V" : "V", "W" : "W", "X" : "X", "Y" : "Y", "1" : "1",
        "8" : "8", "E" : "3", "J" : "L", "S" : "2", "Z" : "5", "3" : "E",
        "L" : "J", "2" : "S", "5" : "Z"
            }
    for i in range(len(string)):
        if string[i] not in list(mirror_letters.keys()):
            return False
        if mirror_letters[string[i]] != string[len(string) - i - 1]:
            return False
    return True
    
def check_palindrome(string):
    return string == string[::-1]


S = str(input("Enter string: "))
text = ""
pal = check_palindrome(S)
mir = check_mirror(S)
if pal:
    if mir:
        text = "is a mirrored palindrome"
    else:
        text = "is a regular palindrome"
else:
    if mir:
        text = "is a mirrored string"
    else:
        text = "is not a palindrome"

print(f"{S} {text}")

