ex_date=int(input("enter a ex date: "))
re_date=int(input("enter a re date: "))
ex_month=int(input("enter ex month: "))
re_month=int(input("enter re month: "))
ex_year=int(input("enter ex year: "))
re_year=int(input("enter re year:"))
if ex_year==re_year:
    if ex_date>=re_date:
        if ex_month==re_month:
            print("no fine")
        if ex_month<re_month:
            print((re_month-ex_month)*30*500) 
    if ex_date<re_date:
        print((re_date-ex_date)*15)           
else:
    print("fine 10000")

