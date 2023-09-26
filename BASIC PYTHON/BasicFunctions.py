from array import *

cars=["Ford","Volvo","BMW"]
cars.append("Honda")
print(cars)

cars.insert(1,"toyta")
print(cars)

cars.pop(1)
print(cars)

cars.remove("Volvo")
print(cars)

x=cars.count("Honda")
print(x)


fruits=["apple","banana","cherry"]

fruits.extend(cars)
print(fruits)

y=fruits.index("cherry")
print(x)

cars.sort()
print(cars)

cars.reverse()
print(cars)

str1="Sakib Hossain "
str2="Subrina Islam Prity"
str3="Sakib Hossain "
print(str1==str2)
print(str1==str3)

result = str1+str2
print(result)
print(len(str1))

print(str2.upper())
print(str2.lower())


#2D Array:
T=[[11,12,5,2],[15,6,10],[10,8,12,5],[12,15,8,6]]
for r in T:
    for c in r:
        print(c,end =" ")
    print()