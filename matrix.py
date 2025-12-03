# 3D matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"Element at [1] [2]: {matrix[1][2]}")

print("Matrix elements:")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()