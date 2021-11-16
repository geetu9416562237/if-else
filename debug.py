'''day=input("kon sa day hai? monday/tuesday")
time=input("kon se time ka khana banrha h lunch/dinner")
if day=="monday" and time=="dinner":
    print("sabji roti")
elif day=="tuesday" and time=="dinner":
    print("aalu k paranthe")
else:
    ("chatni roti")'''
day=input("kon sa day hai? monday/tuesday")
time=input("kon se time ka khana banrha h lunch/dinner")
if day=="monday":
    if time=="lunch":
        print("rajma chawal")
    elif time=="dinner":
        print("roti sabji")
elif day=="tuesday":
    if time=="dinner":
        print("paav bhaji")
    else:
        print("Khichdi khalo bhayi")
else:
    print("maggie hi kha lena")

            
                    


