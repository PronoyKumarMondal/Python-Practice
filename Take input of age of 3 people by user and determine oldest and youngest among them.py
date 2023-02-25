a=input("People 1 age:")
b=input("People 2 age:")
c=input("People 3 age:")

if a>b and a>c:
    if b>c:
        print("Oldest: "+a)
        print("Youngest: "+c)
    else:
        print("Oldest: "+a)
        print("Youngest: "+b)
elif b>a and b>c:
    if a>c:
        print("Oldest: "+b)
        print("Youngest: "+c)
    else:
        print("Oldest: "+b)
        print("Youngest: "+a)
else:
    if a>b:
        print("Oldest: "+c)
        print("Youngest: "+b)
    else:
        print("Oldest: "+c)
        print("Youngest: "+b)
