square=lambda x:x*x
rectangle= lambda x,y:x*y
triangle=lambda x,y:0.5*x*y
a=int(input("enter side of square:"))
print("area of square",square(a))
l=int(input("enter length of rectangle:"))
w=int(input("enter width of rectangle:"))
print("area of rectangle",rectangle(l,w))
b=int(input("enter base of triangle:"))
h=int(input("enter height of triangle:"))
print("area of triangle",triangle(b,h))
