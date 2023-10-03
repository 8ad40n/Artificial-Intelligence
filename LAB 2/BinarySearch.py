def binary_search(arr, item, n):
  low = 0
  high = n - 1
  while low <= high:
    mid = (low + high) // 2
    if item < arr[mid]:
      high = mid - 1
    elif item > arr[mid]:
      low = mid + 1
    else:
      return mid
  return -1

arr = [4, 10, 15, 30, 40]
item = 15
n = len(arr)
arr.sort()
result = binary_search(arr, item, n)
if result != -1:
  print("The element is found at index ",result)
else:
  print("The element is not found in the array.")

