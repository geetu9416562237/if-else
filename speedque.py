#Question - if speed is less than 60 than print "km hai" if speed is less than 30 then "bht km hai" 
#more than 100 then print "bht jyda h"
speed=int(input("gadi ki speed dalo:"))
if speed<=30:
    print("bht km h")
elif speed<=60 and speed>30:
    print("speed kam h")
elif speed>=100:
    print("bht jyda hai")
    
