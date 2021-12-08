d={"January":31,"Februaary":28,"March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"September":30,"October":31,"November":30,"December":31}
sd=sorted(d)
print("sorted in acending order:",sd)
month=input("Enter a month:")
days=d[month]
print("Number of days in",month,"=",days)
r=sorted(d.items(),reverse=True)
print("Months in reverse order:",r)

