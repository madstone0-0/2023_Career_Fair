import sys
from utils import read_csv, find_tri_area, is_inside_tri, write_csv, find_length
from itertools import combinations


def main():
    # Read the command line arguments
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: FindSafeSurrounding.py <filename>")
        sys.exit(1)

    filename = args[0]
    # Read the csv file and store the coordinates in a list
    dataset = read_csv(filename)
    victim = dataset[0]
    del dataset[0]

    triangles = [item for item in combinations(dataset, 3)]
    areas = {}

    for triangle in triangles:
        areas[triangle] = find_tri_area(*triangle)

    min_tri = [(), 99999999]
    for point in dataset:
        for triangle, area in areas.items():
            if not is_inside_tri(point, triangle):
                if is_inside_tri(victim, triangle):
                    if area < min_tri[1]:
                        min_tri = [triangle, area]

    sorted_by_closest = sorted(dataset, key=lambda d: find_length(victim, d))
    result = (
        sorted(min_tri[0], key=lambda c: (c[0], c[1]))
        if min_tri[0]
        else sorted_by_closest[:2]
    )

    write_csv("safesurrounding", result)


if __name__ == "__main__":
    main()
