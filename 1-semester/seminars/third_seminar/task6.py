import numpy as np

# function for calculating least sqaures coeffitients
def mnk(x, y):
    n = len(x)
    a = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x ** 2) - np.sum(x) ** 2)
    b = (np.sum(y) - a * np.sum(x)) / n
    
    return a, b


def main():
    x_input = np.array(input("Insert X values: \n").split())
    x_input = x_input.astype(float)

    y_input = np.array(input("Insert Y values: \n").split())
    y_input = y_input.astype(float)
    if len(x_input) != len(y_input):
        print("Error, array sizes do not match")
        return 1
    a, b = mnk(x_input, y_input)
    print(f"Slope: {a} \nY-interception: {b}")
if __name__ == "__main__":
    main()

