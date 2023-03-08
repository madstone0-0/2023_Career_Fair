import sys
import itertools


def find_length(coords1: tuple, coords2: tuple) -> float:
    """
    Calculates the distance between two coordinates using the formula
    sqrt((x1-x2)^2 + (y1-y2))
    :param coords1:
    :param coords2:
    :return: length
    """
    return ((coords1[0] - coords2[0]) ** 2 + (coords1[1] - coords2[1]) ** 2)**(1/2)


def find_area(coords1: tuple, coords2: tuple, coords3: tuple) -> float:
    """
    Calculates the area of the triangle using Heron's Formula, where
    a, b, and c are the lengths of the sides and s is half the perimeter
    of the triangle, i.e. (a + b + c) / 2
    Area = sqrt( s(s-a)(s-b)(s-c) )
    :param coords1:
    :param coords2:
    :param coords3:
    :return: area
    """
    a = find_length(coords1, coords2)
    b = find_length(coords2, coords3)
    c = find_length(coords3, coords1)
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c))**(1/2)

args = sys.argv[1:]
if len(args) == 0:
    print("Usage: FindSafeTriangle.py <filename>")
    sys.exit(1)

filename = args[0]
with open(filename, mode="r", encoding="utf-8") as file:
    dataset = [ (float(line.split(",")[0]), float(line.split(",")[1].strip("\n"))) for line in file.readlines()[1:] ]

# A dict object for storing calculated areas and their
# triangle's coordinates
areas = {}

# Using the builtin itertools combination method to generate
# all possible coordinate combinations without replacement
triangles = itertools.combinations(dataset, 3)
for triangle in triangles:
    areas[(triangle[0], triangle[1], triangle[2])]=find_area(triangle[0], triangle[1], triangle[2])

# Retrieving the dict key (triangle coords) with the maximum area and
# sorting the coords using the sorted function setting the key as an anonymous
# function sorting the coords smallest to the biggest first by x-coord then y-coord
largest_area = sorted(max(areas, key=areas.get), key=lambda c: (c[0], c[1]))

# Write triangle coords with the largest area to safetriangle.csv
with open("safetriangle.csv", mode="w+", encoding="utf-8") as file:
    string = "x,y\n"
    for coord in largest_area:
        string += f"{coord[0]},{coord[1]}\n"
    file.write(string)

