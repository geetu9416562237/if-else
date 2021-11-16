A=int(input("enter a number: "))
B=int(input("enter a number: "))
ch=input("enter an operater: ")
if ch=='+':
    print(A+B)
elif ch=="-":
    print(A-B)
elif ch=="/":
    print(A/B)
elif ch=="*":
    print(A*B)
elif ch=="//":
    print(A//B)
elif ch=="%":
    print(A%B)
else:
    print(A**B)
