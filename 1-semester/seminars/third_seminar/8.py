import random
import numpy as np
from task6 import mnk

def generate(n, a, b):
    x = []
    values = []
    for i in range(n):
        x.append(i)
        y = a * i + b
        noise = random.gauss(0, 1)
        values.append(y + noise)

    return np.array(x), np.array(values)


def main():
    n = int(input("Enter N: "))
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))

    x, y = generate(n, a, b)
    a_calcul, b_calcul = mnk(x, y)

    print(f"Calculated\na: {a_calcul};\nb: {b_calcul}.")

main()
    
