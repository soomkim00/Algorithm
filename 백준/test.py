point = [[1, 2, 3], [4, 5, 6]]
m = 1
for i in range(3):
    point[m][i] = point[m][i] - 1 if point[m][i] >= 1 else 7

print(point)
