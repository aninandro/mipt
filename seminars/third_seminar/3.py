

def euclid(a, b):
    if b == 0:
        return a
    return euclid(b, a % b)


def main():
    string = input("Enter numbers: ")
    nums = string.split()
    a = int(nums[0])
    b = int(nums[1])

    d = euclid(a,b)
    print(d)
    return 0

main()
