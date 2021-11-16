year=int(input("enter a year: "))
if year%400==0:
    print("century")
elif year%4==0:
    print("leap year")
elif year%100!=0:
    print("leep year")


