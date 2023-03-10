import itertools
import sys

from utils import read_csv, find_poly_area, find_tri_area, write_csv, is_convex


def main():
    # Read the command line arguments
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: FindSafePolygon.py <filename>")
        sys.exit(1)

    filename = args[0]
    # Read the csv file and store the coordinates in a list
    dataset = read_csv(filename)

    # Generate all possible triangle and polygon combinations
    # Using the builtin itertools combination method
    triangles = itertools.combinations(dataset, 3)
    polygons = itertools.combinations(dataset, 4)

    # Dict objects for storing calculated areas and their
    # shaoe's coordinates
    tri_areas = {}
    pol_areas = {}

    # Calculate the area of each triangle
    for triangle in triangles:
        tri_areas[triangle] = find_tri_area(*triangle)

    # Calculate the area of each polygon
    for polygon in polygons:
        if is_convex(polygon):
            pol_areas[polygon] = find_poly_area(*polygon)

    # Retrieving the dict key (shape coords) with the maximum area and
    # sorting the coords using the sorted function setting the key as an anonymous
    # function sorting the coords smallest to the biggest first by x-coord then y-coord
    # This time storing the key with the largest area in a variable to be used later
    max_tri_key = max(tri_areas, key=tri_areas.get)
    max_triangle = sorted(max_tri_key, key=lambda c: (c[0], c[1]))

    max_pol_key = max(pol_areas, key=pol_areas.get)
    max_polygon = sorted(max_pol_key, key=lambda c: (c[0], c[1]))

    # Write shape coords with the largest area to safepolygon.csv
    # If there are no polygons, write the triangle with the largest area
    # Or if there are polygons but the triangle has a larger area, write the triangle's coords
    # to safepolygon.csv and exit the program
    if not pol_areas or tri_areas[max_tri_key] > pol_areas[max_pol_key]:
        write_csv("safepolygon", max_triangle)
        sys.exit(0)

    # If there are polygons and the polygon has a larger area, write the polygon's coords
    write_csv("safepolygon", max_polygon)


if __name__ == "__main__":
    main()
