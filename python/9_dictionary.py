#create dictionary to store 20 different detail about your ownself 
student = {'name':'jayesh kucha','age':21,'weight':51.25,'gender':True,'degree':None,'degree':'BCA','dob':23/5/2006,'address':'trapaj','city':'bhavnagr', "state": "Gujarat","mobile": "9999999999", "college": "ssccm", "course": "BCA",}

#print dictionary
print(student)

#print name, age, gender, dob 
print(student['name'])
print(student['age'])
print(student['gender'])
print(student["dob"])

#add key value pair pincode into dictionary
student['pincode'] = 364110
print(student)

#add key value pair to store your 5 favourite touriest destination 
student['favourite_touriest_destination'] = ['gova','Jaipur','kashmir','kerala','manali']
print(student)

#print all the favourite touriest destination 
print(student['favourite_touriest_destination'])

#use update method to add new key value pair in dictionary
student.update({'hobby':['coding']})
print(student)

#use update method to change existing key value pair in dictionary
student.update({"age": 24})
print(student)

#use pop method to remove dob 
student.pop('dob')
print(student)

#use popitem item method to remove last item 
student.popitem()
print(student)

#display all keys
print(student.keys())
print(student)

#display all values 
print(student.values())
print(student)

#copy dictionary to another dictionary using copy function 
student2=student.copy()

print(student2)

#clear newly create dictionary

student2.clear()

print(student,student2)

print("GOOD BYY :):)")
