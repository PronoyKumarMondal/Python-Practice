c=int(input())
p=int(input())
t=((c*120)+(p*75))

if(t>=300 and t<=499):
    print("Privious total: "+str(t))
    print("New total after discount: "+str(t-10))
elif(t>=500 and t<=749):
        print("Privious total: "+str(t))
        print("New total after discount: "+str(t-20))
elif(t>=750 and t<=999):
        print("Privious total: "+str(t))
        print("New total after discount: "+str(t-50))
elif(t>=1000):
        print("Privious total: "+str(t))
        print("New total after discount: "+str(t-150))
else:
        print("Privious total: "+str(t))
        print("New total after discount: "+str(t))

