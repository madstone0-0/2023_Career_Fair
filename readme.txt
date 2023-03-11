Madiba Hudson-Quansah, Class of 2026

FindSafeTriangle.py

Usage: python3 ./FindSafeTriangle.py <filename>
Tested on: Python 3.11.2 and 3.10.6
Requirements: Python 3.7+
Supports: 
Generating all possible triangles from a given list of coordinates
Calculating the area of each generated triangle
Recording the combination with the largest area and writing it to safetriangle.csv

FindSafePolygon.py

Usage: python3 ./FindSafePolygon.py <filename>
Tested on: Python 3.11.2 and 3.10.6
Requirements: Python 3.7+
Supports:
Generating all possible polygons (with a limit of four points) from a given list of coordinates
Calculating the area of each generated polygon
Comparing the area of the largest polygon and compromising triangles
Recording the result with the max area and writing it to safepolygon.csv

FindSafeSurrounding.py
Usage: python3 ./FindSafeSurrounding.py <filename>
Tested on: Python 3.11.2 and 3.10.6
Requirements: Python 3.7+
Supports:
Isolating location of a survivor.
Generating all possible triangles.
Determining the smallest triangular area, the survivor is located in if possible.
If the smallest triangular area cannot be determined, the closest two points are instead returned.
Records the coordinates of the smallest triangular area or closest two points to the file safesurrounding.csv
