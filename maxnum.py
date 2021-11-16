#How to find Max number between three number
Num1=int(input("enter a number:"))
Num2=int(input("enter a number:"))
Num3=int(input("enter a number:"))
if Num1>Num2 and Num1>3:
    print("num1 is Max")
elif Num2>Num1 and Num2>Num3:
    print("Num2 is Max")
else:
    print("Num3 is max")
