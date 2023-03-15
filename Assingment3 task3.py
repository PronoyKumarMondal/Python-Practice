n=input()
l=len(n)
f=0
i=0
for i in range(l-1):
    if n[i]=='0' or n[i]=='1':
        f=0
    else:
        f=1
        break
if f==0:
    print("Binary Number")
else:
    print("Not a Binary Number")
    