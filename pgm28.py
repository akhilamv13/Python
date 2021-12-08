n=int(input("enter a number:"))
n1=int(input("enter another number:"))
b=min(n,n1)
a=0
for i in range(1,b+1):
    if(n%i==0 and n1%i==0):
        if(a<i):
            a=i
print(i)
