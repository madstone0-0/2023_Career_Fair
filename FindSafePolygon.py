import sys
from utils import read_csv


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: FindSafePolygon.py <filename>")
        sys.exit(1)

    filename = args[0]
    dataset = read_csv(filename)


if __name__ == "__main__":
    main()
