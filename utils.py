import csv


def find_length(coords1: tuple, coords2: tuple) -> float:
    """
    Calculates the distance between two coordinates using the formula
    sqrt((x1-x2)^2 + (y1-y2))
    :param coords1:
    :param coords2:
    :return: length
    """
    return ((coords1[0] - coords2[0]) ** 2 + (coords1[1] - coords2[1]) ** 2) ** (1 / 2)


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
    return (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)


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


def write_csv(filename: str, coords: list) -> None:
    """
    Writes a list of tuples to a csv file
    :param filename:
    :param coords:
    :return: None
    """
    with open(f"{filename}.csv", mode="w+", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["x", "y"])
        writer.writerows(coords)
