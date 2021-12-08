farm={"sheeps":5,"cows":2,"goats":10}
print("elements in dictionary:",farm)
d={"ducks":8}
farm.update(d)
print("elements in dictionary after update:",farm)
c=len(farm)
print("number of items in dictionary:",c)
del(farm['cows'])
print("elements in dictionary :",farm)
