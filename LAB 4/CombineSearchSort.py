def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]

		mergeSort(L) 
		mergeSort(R)

		i = j = k = 0

		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1


def partition(array, low, high):

	pivot = array[high]

	i = low - 1

	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])

	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1

def quicksort(array, low, high):
	if low < high:
		pi = partition(array, low, high)
		quicksort(array, low, pi - 1)
		quicksort(array, pi + 1, high)



def linearSearch(arr,item):
    i=0
    while(i<len(arr)):
        if arr[i]==item:
            print("Found in index",i)
        i=i+1
        
def binarySearch(arr,item,n):
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
item = 30
option=2
print("Option 1: Linear search")
print("Option 2: Binary search")
print()
print("You have choosen option ",option)
if(option==1):
    linearSearch(arr,item)
elif(option ==2):
    n = len(arr)
    op=2
    print("Option 1: Merge Sort")
    print("Option 2: Quick search")
    print()
    print("You have choosen option ",op)
    print()
    print()
    
    if(op==1):
        mergeSort(arr)
    elif(op==2):
        quicksort(arr, 0, len(arr) - 1)
        

    result = binarySearch(arr, item, n)
    if result != -1:
        print(item," is at index ",result)
    else:
        print(item," is not available in the array.")

print()
print()
        
