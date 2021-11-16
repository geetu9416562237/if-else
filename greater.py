'''n=int(input("enter a number:"))
n1=int(input("enter a number:"))
if n>n1:
    print("n is greater")
else:
    print("n1 is greater")'''
'''Number=int(input("enter a number"))
if Number%5==0 and Number%15==0:
    print("dono se divisble hai") 
else:
    print("divisble nhi hai")'''
n=int(input("enter the number:"))
if n%5==0:
    print("its is divisible by 5")
    if n%15==0:
        print("it is divisble with 15")
        if n%10==0:
            print("divisble hai 10 se")
        else:
            print("10 se divisble nhi hai")
    else:
        print("it is not divisbel with 15")
else:
    print("it is not divisble with 5")
