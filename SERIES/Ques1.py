import csv 
dict_value = [
{'Name': 'AKHILA', 'MFC': 45,'DC':35,'DS':40,'ASE':30},
{'Name': 'ARCHITHA', 'MFC': 40,'DC':'25','DS':'30','ASE':'30'},
{'Name': 'AKSHITHA', 'MFC': 50,'DC':15,'DS':45,'ASE':38},
{'Name': 'ARCHANA', 'MFC': 25,'DC':23,'DS':30,'ASE':31},
{'Name': 'APARNA', 'MFC': 46,'DC':42,'DS':34,'ASE':28},
{'Name': 'ARATHY', 'MFC': 40,'DC':32,'DS':29,'ASE':27},
{'Name': 'SREELAKSHMI', 'MFC': 48,'DC':37,'DS':42,'ASE':39},
{'Name': 'KANAGA', 'MFC': 42,'DC':45,'DS':41,'ASE':37},
{'Name': 'DHANYA', 'MFC': 48,'DC':44,'DS':25,'ASE':24},
{'Name': 'BHAVYA', 'MFC': 50,'DC':35,'DS':47,'ASE':39}]
print("\n\nStudent Names and marks:\n")
fields = ["Name","MFC","DC","DS","ASE"]

with open('stud.csv','w') as c:
    writer = csv.DictWriter(c,fieldnames=fields)
    writer.writeheader()
    writer.writerows(dict_value)
    c.close()
mfc=0
dc=0
ase=0
ds=0
n=0
with open('dict.csv', 'r') as csvread:
    reader= csv.DictReader(csvread)
    for data in reader:
        if n==0:
            print(f'{"  ".join(data)}')
            n=n+1
        print(f'{data["Name"]}{data["MFC"]} {data["DC"]} {data["DS"]} {data["ASE"]}' )
with open('stud.csv','r') as csvread:
     reader = csv.DictReader(csvread)
     print("\n\nStudent Names and Percentage:\n")
     for row in reader:
         print(row['Name'],":",(int(int(row['MFC'])+int(row['DC'])+int(row['DS'])+int(row['ASE']))/200)*100)
         mfc=mfc+int(row['MFC'])
         dc=dc+int(row['DC'])
         ase=ase+int(row['ASE'])
         ds=ds+int(row['DS'])
print("\nAverage of subjects\n")
print("MFC",mfc/10)
print("DC",dc/10)
print("DS",ds/10)
print("ASE",ase/10)
