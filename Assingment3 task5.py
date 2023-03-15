n=input()
l=len(n)
for i in range(1,l+1):
    for j in range(i):
        print(n[j],end="")
    print()