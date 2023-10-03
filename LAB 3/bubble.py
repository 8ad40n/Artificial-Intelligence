def Bubble(array):
  swapped = True
  while swapped:
    swapped = False

    i = 0
    while i < len(array) - 1:
      if array[i] > array[i + 1]:
        array[i], array[i + 1] = array[i + 1], array[i]
        swapped = True
      i += 1
  return array

array = [5, 3, 2, 1, 4]
sorted_array = Bubble(array)
print(sorted_array)
