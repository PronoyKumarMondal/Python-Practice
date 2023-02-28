h=int(input())

if h>=4 and h<=6:
    print("Breakfast")
elif h>=12 and h<=13:
    print("Lunch")
elif h>=16 and h<=17:
    print("Snacks")
elif h>=19 and h<=20:
    print("Dinner")
else:
    if h<0 or h>23:
        print("Wrong time") 
    else:
        print("Patience is a virtue")
