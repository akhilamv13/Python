l=[]
l1=[]
l2=[]
n=int(input("enter the number of elements in first list:"))
for i in range(1,n+1):
    x=int(input())
    l.append(x)
n1=int(input("enter the number of elements in first list:"))
for i in range(1,n1+1):
    x=int(input())
    l1.append(x)
print(l)
print(l1)
s=len(l)
s1=len(l1)
if(s==s1):
    print("Two lists are of same lenth:",s1)
else:
    print("Two lists are of different lenth.\nLength of first list:",s,"Length of second list:",s1)
a=sum(l)
print("sum of first list:",a)
a1=sum(l1)
print("sum of second list:",a1)
if(a==a1):
    print("Sum of two list are same")
else:
    print("Sum of two list are different")
print("Same numbers in both list:")
for i in l:
    for j in l1:
        if(i==j):
            l2.append(i)
if(len(l2)==0):
    print("No same elements in ")
else:
    print(l2)
            
    
    
            
            
        
    
