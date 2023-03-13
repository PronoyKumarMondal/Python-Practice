n=int(input())
i=0
while i<n:
    k=input()
    if len(k)<11:
        print(k)
    else:
        l=len(k)-2
        print(k[0]+str(l)+k[-1])
    i+=1