import numpy as np

def make_matrix(n, m):
    return np.zeros((n,m))


def fill_matrix(matrix, n, m):
    top = 0
    bottom = n - 1
    left = 0
    right = m -1
    x_cursor = 0
    y_cursor = 0
    value = 1

    while value <= n * m:
        while x_cursor <=  right:
            matrix[y_cursor][x_cursor] = value
            x_cursor += 1
            value += 1
        x_cursor -= 1
        y_cursor += 1
        while y_cursor <= bottom:
            matrix[y_cursor][x_cursor] = value
            y_cursor += 1
            value += 1
        y_cursor -= 1
        x_cursor -= 1
        if top > bottom:
            break
        while x_cursor >= left:
            matrix[y_cursor][x_cursor] = value
            x_cursor -= 1
            value += 1
        x_cursor += 1
        y_cursor -= 1
        if left > right:
            break
        while y_cursor > top:
            matrix[y_cursor][x_cursor] = value
            y_cursor -= 1
            value += 1
        y_cursor += 1
        x_cursor += 1

        right -= 1
        left += 1
        bottom -= 1
        top += 1
    
    return matrix
def main():
    user_input = input("Enter N and M: ").split()
    n = int(user_input[0])
    m = int(user_input[1])
    matrix = make_matrix(n, m)
    matrix = fill_matrix(matrix, n, m)
    rows = np.array([[i] for i in range(0, n)])
    matrix = matrix * rows
    print(matrix)

main()
