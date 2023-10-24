def bubble_sort(products):
    n = len(products)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if products[j][1] > products[j + 1][1]:
                products[j], products[j + 1] = products[j + 1], products[j]
                swapped = True
        if not swapped:
            break

products = [("Product A", 25), ("Product B", 15), ("Product C", 30), ("Product D", 10)]
bubble_sort(products)

for product in products:
    print(f"{product[0]} - ${product[1]}")
