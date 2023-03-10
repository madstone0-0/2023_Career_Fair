import sys
import itertools
from utils import find_tri_area, read_csv, write_csv


def main():
    # Read the command line arguments
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: FindSafeTriangle.py <filename>")
        sys.exit(1)

    filename = args[0]
    # Read the csv file and store the coordinates in a list
    dataset = read_csv(filename)

    # A dict object for storing calculated areas and their
    # triangle's coordinates
    areas = {}

    # Using the builtin itertools combination method to generate
    # all possible coordinate combinations without replacement
    triangles = itertools.combinations(dataset, 3)
    for triangle in triangles:
        areas[triangle] = find_tri_area(*triangle)

    # Retrieving the dict key (triangle coords) with the maximum area and
    # sorting the coords using the sorted function setting the key as an anonymous
    # function sorting the coords smallest to the biggest first by x-coord then y-coord
    largest_area = sorted(max(areas, key=areas.get), key=lambda c: (c[0], c[1]))

    # Write triangle coords with the largest area to safetriangle.csv
    write_csv("safetriangle", largest_area)


if __name__ == "__main__":
    main()
