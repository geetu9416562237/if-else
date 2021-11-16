basic_salary=int(input("enter a basic sallary: "))
if basic_salary<=10000:
    HRA=20/100*basic_salary
    DA=80/100*basic_salary
    GROSS=basic_salary+HRA+DA
    print(GROSS)
