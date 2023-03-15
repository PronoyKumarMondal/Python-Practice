n=input()
l=len(n)
for i in range(0,l-1):
    if n[i]!=n[i+1]:
        print(n[i],end="")
        if i==l-2:
            print(n[i+1])