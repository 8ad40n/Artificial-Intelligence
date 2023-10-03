def triangle(a,b,c):
    s = (a + b + c) / 2  
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
    print(area)

triangle(10,10,10)
    