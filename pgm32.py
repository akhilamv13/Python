l=[]
n=int(input("enter the limit:"))
for i in range(1,n+1):
    x=int(input())
    l.append(x)
print(l)
s=0
for i in l:
    s=s+i
print("sum of items in the list:",s)
