age=int(input("enter a age: "))
employee=input("enter employee is male or female: ")
if employee=="female":
    print("she will work only in urban areas")
elif employee=="male" and age>=20 and age<=40:
    print("He may work anywhere")
elif employee=="male" and age>=40 and age<=60:
    print("he will work in urban areas only")
else:
    ("ERROR")
        