l=[]
n=int(input("Enterthe limit:"))
print("enter",n,"words")
for i in range(1,n+1):
    s2=input()
    l.append(s2)
b=0
for x in l:
    c=len(x)
    if(b<c):
        b=c
        s3=x
print("longest word and it's length is -",s3,":",b)
    
