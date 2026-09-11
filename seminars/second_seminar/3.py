def check_mirror(string):
    mirror_letters = ["A","H","I","M","O","T","U","V","W","X","Y","1","8","E","J","S","Z","3","L","2","5"]
    if all(x in mirror_letters for x in string):
        return True
    return False
    
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

