arr=[2,1,3,4,5,6]
high=len(arr)
low=0

middle=int((high-low)/2)
arr.insert(middle,10)
print(arr)