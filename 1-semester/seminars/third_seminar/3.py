
def euclid(a, b):
    if b == 0:
        return 1, 0, a
    x1, y1, d = euclid(b, a % b)

    x = y1
    y = x1 - (a // b) * y1
    return x, y, d

def main():
    string = input("Enter numbers: ")
    nums = string.split()
    a = int(nums[0])
    b = int(nums[1])
    result = euclid(a, b)
    print(f"{result[0]} {result[1]} {result[2]}")

main()

