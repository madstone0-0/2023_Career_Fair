import csv


def find_length(coords1: tuple, coords2: tuple) -> float:
    """
    Calculates the distance between two coordinates using the formula
    sqrt((x1-x2)^2 + (y1-y2))
    :param coords1:
    :param coords2:
    :return: length
    """
    return round(
        ((coords1[0] - coords2[0]) ** 2 + (coords1[1] - coords2[1]) ** 2) ** (1 / 2), 3
    )


def find_cross_prod(pol):
    """
    Calculates the cross product of two vectors
    :param pol:
    :return:
    """
    x1 = pol[1][0] - pol[0][0]
    y1 = pol[1][1] - pol[0][1]

    x2 = pol[2][0] - pol[0][0]
    y2 = pol[2][1] - pol[0][1]

    return x1 * y2 - y1 * x2


def find_tri_area(coords1: tuple, coords2: tuple, coords3: tuple) -> float:
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
    return round((s * (s - a) * (s - b) * (s - c)) ** (1 / 2), 3)


def find_poly_area(
    coords1: tuple, coords2: tuple, coords3: tuple, coords4: tuple
) -> float:
    """
    Calculates the area of a polygon using the Shoelace Formula, i.e.
    A = 1/2 * abs( x1y2 + x2y3 + x3y4 + x4y1 - y1x2 - y2x3 - y3x4 - y4x1 )
    :param coords1:
    :param coords2:
    :param coords3:
    :param coords4:
    :return:
    """
    a = coords1[0] * coords2[1] - coords1[1] * coords2[0]
    b = coords2[0] * coords3[1] - coords2[1] * coords3[0]
    c = coords3[0] * coords4[1] - coords3[1] * coords4[0]
    d = coords4[0] * coords1[1] - coords4[1] * coords1[0]

    return round(1 / 2 * abs(a + b + c + d), 3)


def is_convex(polygon: tuple) -> bool:
    """
    Checks if a polygon is convex by calculating the cross product of
    three consecutive points in the polygon. If the cross product is
    positive, the polygon is convex, otherwise it is concave.
    :param polygon:
    :return:
    """
    n = len(polygon)
    prev = 0
    curr = 0

    for i in range(n):
        temp = [polygon[1], polygon[(i + 1) % n], polygon[(i + 2) % n]]
        curr = find_cross_prod(temp)
        if curr != 0:
            if curr * prev < 0:
                return False
            else:
                prev = curr
    return True


def is_inside_tri(point: tuple, triangle: tuple) -> bool:
    """
    Checks if a point is inside a triangle by calculating the area of
    the triangle and the sum of the areas of the three triangles
    formed by the point and the three vertices of the triangle.
    If the sum of the areas is equal to the area of the triangle,
    the point is inside the triangle, otherwise it is outside.
    :param point:
    :param triangle:
    :return:
    """
    # Check if point is one of the vertices
    # If it is, it is not inside the triangle.
    if any([point == x for x in triangle]):
        return False

    a = find_tri_area(*triangle)
    a1 = find_tri_area(point, triangle[0], triangle[1])
    a2 = find_tri_area(point, triangle[1], triangle[2])
    a3 = find_tri_area(point, triangle[0], triangle[2])
    return a == (a1 + a2 + a3)


def read_csv(filename: str) -> list:
    """
    Reads a csv file and returns a list of tuples containing
    x and y coordinates
    :param filename:
    :return: list of tuples
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        return [(float(row[0]), float(row[1])) for row in reader]


def write_csv(filename: str, coords: list | tuple) -> None:
    """
    Writes a list of tuples to a csv file
    :param filename:
    :param coords:
    :return: None
    """
    with open(f"{filename}.csv", mode="w+", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["x", "y"])
        writer.writerows(coords)
