def selection_sort(products):
    n = len(products)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if products[j][1] < products[min_index][1]:
                min_index = j
        products[i], products[min_index] = products[min_index], products[i]


products = [("Dairy Milk", 50), ("Kitkat", 75), ("Ice cream", 60), ("Mountain Dew", 20)]
selection_sort(products)

for product in products:
    print(f"{product[0]} - BDT {product[1]}")
