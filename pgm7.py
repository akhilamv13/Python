s=input("Enter a string:")
n=int(input("Enter index to be removed:"))
l=len(s)
a=s[0:n]
b=s[n+1:l]
snew=a+b
print(snew)
