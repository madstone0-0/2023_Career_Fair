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
    # Remove the victim's coords from the list
    victim = dataset[0]
    del dataset[0]

    # Generate triangles from the remaining coords
    triangles = [item for item in combinations(dataset, 3)]
    areas = {}

    # Find the area of each triangle
    for triangle in triangles:
        areas[triangle] = find_tri_area(*triangle)

    # Find the triangle with the smallest area
    min_tri = [(), 99999999]
    # Iterate through the dataset and check if the point is inside the triangle
    for point in dataset:
        for triangle, area in areas.items():
            # If no other points are inside the area of the triangle
            # check if the victim is inside the area of the triangle
            if not is_inside_tri(point, triangle):
                # If the victim is inside the triangle check if the
                # area of the triangle is smaller than the one previously stored
                if is_inside_tri(victim, triangle):
                    if area < min_tri[1]:
                        min_tri = [triangle, area]

    # Sort dataset by points closest to victim using the length of a line
    # joining those two points
    sorted_by_closest = sorted(dataset, key=lambda d: find_length(victim, d))

    # If a minimum triangle has been found write the coords of it vertexes to
    # safesurrounding.csv else write the two closest points to the victim
    result = (
        sorted(min_tri[0], key=lambda c: (c[0], c[1]))
        if min_tri[0]
        else sorted_by_closest[:2]
    )

    write_csv("safesurrounding", result)


if __name__ == "__main__":
    main()
