import pandas as pd
import numpy as np
import sys


def find_length(coords1: tuple, coords2: tuple) -> float:
    return np.sqrt((coords1[0] - coords2[0]) ** 2 + (coords1[1] - coords2[1]) ** 2)


def find_area(coords1: tuple, coords2: tuple, coords3: tuple) -> float:
    a = find_length(coords1, coords2)
    b = find_length(coords2, coords3)
    c = find_length(coords3, coords1)
    s = (a + b + c) / 2
    return np.sqrt(s * (s - a) * (s - b) * (s - c))


if len(sys.argv) != 2:
    print("Usage: FindSafeTriangle.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
dataset = pd.read_csv(filename)

print(dataset)
