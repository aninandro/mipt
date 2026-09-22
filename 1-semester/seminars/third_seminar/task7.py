import numpy as np


def main():
    n = int(input("Insert N: "))
    m = int(input("Insert M: "))
    matrix = []
    for _ in range(n):
        line = np.array(input("Enter M numbers: \n").split()).astype(float)
        matrix.append(line)
        print("\n")
    matrix = np.array(matrix)
    values = matrix[:, -1].reshape(-1)
    coefs = matrix[:, :-1]
    result = np.linalg.solve(coefs, values)
    print(result)

main()
