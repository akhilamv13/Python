n=int(input("Enter number:"))
a=n
s=0
while(n!=0):
    r=n%10
    s=s+r
    n=int(n/10)
print("sum of digits of",a,"is",s)
