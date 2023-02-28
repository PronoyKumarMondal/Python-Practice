a=int(input())
b=int(input())
a=(a/1000)

b=(b/3600)

if (a/b)<60:
    print(str(a/b)+"km/h"+"\nToo slow. Needs more changes.")
elif (a/b)>=60 and (a/b)<=90:
    print(str(a/b)+"km/h"+"\nVelocity is okay. The car is ready!")
else:
    print(str(a/b)+"km/h"+"\nToo fast. Only a few changes should suffice.")