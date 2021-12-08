l=[]
l1=[]
n=int(input("enter the limit:"))
for i in range(1,n+1):
    x=int(input())
    l.append(x)
print("list:",l)
for j in l:
    if(j>=100):
        l1.append("over")
    else:
        l1.append(j)
print("New list:",l1)
