sum=0
c=0
for i in range(1,11):
    n=int(input())
    if(n%2!=0):
        sum+=n
        c+=1
print("The total of the odd numbers is "+str(sum)+" and their average is "+str(sum/c))