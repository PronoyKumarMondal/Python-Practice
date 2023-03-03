t=int(input())
d=((t-32)*0.56)
if(d==0):
    d=int(d)
if(d<20):
    print(str(d)+" degrees C")
    print("Winter")
elif(d>=20 and d<=25):
    print(str(d)+" degrees C")
    print("Autumn")
elif(d>25 and d<30):
    print(str(d)+" degrees C")
    print("Spring")
elif(d>=30):
    print(str(d)+" degrees C")
    print("Summer")
