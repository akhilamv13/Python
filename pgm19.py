s=input("Enter a string:")
l=s.split()
s1={x:l.count(x) for x in l}
print(s1)
