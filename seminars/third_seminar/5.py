import numpy as np

def make_matrix(n, m):
    x = np.array([0] * n)
    y = np.array([0] * m)
    return x * y

def main():
    stdin = input("Enter N and M: ").split()
    n = int(stdin(0))
    m = int(stdin(0))
    print(make_matrix(n, m))
    return 0

main()
