ex_date=int(input("enter a ex date: "))
re_date=int(input("enter a re date: "))
ex_month=int(input("enter ex month: "))
re_month=int(input("enter re month: "))
ex_year=int(input("enter ex year: "))
re_year=int(input("enter re year"))
if ex_date>re_date and ex_month>re_month and ex_year>re_year:
    print("no fine")
elif ex_date<re_date and ex_month==re_month and ex_year==re_year: 
    n=re_date-ex_date
    fine=n*15
    print("Fine on no of exceeded days",fine)
elif ex_month<re_month and ex_year==re_year:
    print("500 fine")  
elif ex_year<re_year:
    ("10000 FINE")

