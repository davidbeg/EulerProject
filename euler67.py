from pprint import pprint

with open("p067_triangle.txt", "r") as triangle_file:
    data = triangle_file.read()
    triangle = [row.split(" ") for row in data.split("\n")]
    for i in range(len(triangle) - 3, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] = int(triangle[i][j]) + max(int(triangle[i + 1][j]), int(triangle[i + 1][j + 1]))
    pprint(triangle[0][0])
