def houseNo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return houseNo(n-1) + houseNo(n-2)

n = 20
for i in range(n):
    number = houseNo(i)
    print(f"House {i+1}: {number}")

