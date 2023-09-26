m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 6]
]
result = [[0 for _ in range(len(m1))] for _ in range(len(m1[0]))]

for i in range(len(m1)):
    for j in range(len(m1)):
        result[j][i] = m1[i][j]

for row in result:
    print(row)