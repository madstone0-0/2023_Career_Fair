import sys
import itertools


def find_length(coords1: tuple, coords2: tuple) -> float:
    return ((coords1[0] - coords2[0]) ** 2 + (coords1[1] - coords2[1]) ** 2)**(1/2)


def find_area(coords1: tuple, coords2: tuple, coords3: tuple) -> float:
    a = find_length(coords1, coords2)
    b = find_length(coords2, coords3)
    c = find_length(coords3, coords1)
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c))**(1/2)


if len(sys.argv) != 2:
    print("Usage: FindSafeTriangle.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
with open(filename, mode="r", encoding="utf-8") as file:
    dataset = [ (float(line.split(",")[0]), float(line.split(",")[1].strip("\n"))) for line in file.readlines()[1:] ]

areas = {}

triangles = itertools.combinations(dataset, 3)
for triangle in triangles:
    areas[(triangle[0], triangle[1], triangle[2])]=find_area(triangle[0], triangle[1], triangle[2])

largest_area = sorted(max(areas, key=areas.get), key=lambda c: (c[0], c[1]))

with open("safetriangle.csv", mode="w+", encoding="utf-8") as file:
    string = "x,y\n"
    for coord in largest_area:
        string += f"{coord[0]},{coord[1]}\n"
    file.write(string)

