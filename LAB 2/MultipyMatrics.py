m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

if len(m1[0]) != len(m2):
    print("")
else:
    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    for row in result:
        print(row)

