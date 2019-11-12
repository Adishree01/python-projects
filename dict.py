dict={'rollno':[1,2,3,4],'name': ['adi','pranisa','ipsha','jenis']
roll= dict['rollno']
nam= dict['name']
for i in range (len(roll)):
    if roll[i]==3:
        temp=i
print(nam[temp])