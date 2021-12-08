s=[1,2,3,5,4,6,7,8,9]
odd=[]
even=[]
for i in s:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("odd numbers:",odd)
print("even numbers:",even)
    
