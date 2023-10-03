def Selection(array):

  i = 0
  while i < len(array) - 1:
    smallest_index = i
    j = i + 1
    while j < len(array):
      if array[j] < array[smallest_index]:
        smallest_index = j
      j += 1
    array[i], array[smallest_index] = array[smallest_index], array[i]
    i += 1

  return array

array = [5, 3, 2, 1, 4, 5, 1]
sorted_array = Selection(array)
print(sorted_array)
