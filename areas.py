#area of a rectangle
def area (l,w):
    a=l*w
    print("the area is",a)
area (10,20)

#area of a circle
def findArea(r): 
    PI=3.142
    return PI*(r*r)
num=float(input("Enter r value:"))
print("Area is %.6f" % findArea(num))
findArea(num)
