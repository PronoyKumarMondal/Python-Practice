n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
        if i==n:
           print(i)
        else:
            print(i,end=",")
print("Total "+str(c)+" divisors.")
