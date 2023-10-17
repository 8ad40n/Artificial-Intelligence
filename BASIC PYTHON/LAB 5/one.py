def distribute_products(products):
    shelves = [[] for _ in range(5)]  # Create 5 shelves

    for product in products:
      if product[1] <= 20:
        shelves[0].append(product)
      elif product[1] <= 40:
        shelves[1].append(product)
      elif product[1] <= 60:
        shelves[2].append(product)
      elif product[1] <= 80:
        shelves[3].append(product)
      else:
        shelves[4].append(product)

    return shelves


def display_shelves(shelves):
  for i, shelf in enumerate(shelves):
    print(f"Shelf {i + 1}:")
    for product in shelf:
      print(f"Product: {product[0]}, Price: {product[1]}")
    print("-" * 30)


if __name__ == "__main__":
  products = [("Dairy Milk", 50), ("Kitkat", 75), ("Ice cream", 60), ("Mountain Dew", 20)]

  shelves = distribute_products(products)
  display_shelves(shelves)
 