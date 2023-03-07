n=int(input())
a=n
c=0
ans=0
while a>0:
    a=a//10
    c+=1
while n>0:
    ans=(n//(10**c))
    n=(n%(10**c))
    c=c-1
    if(ans!=0):
        print(ans)

    
