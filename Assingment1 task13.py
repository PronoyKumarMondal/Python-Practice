a=int(input())
if(a<0 or a>100):
    print("Invalid Mark")
else:
    if a>=90 and a<=100:
        print("A")
    elif a>=80 and a<=89:
        print("B")
    elif a>=70 and a<=79:
        print("C")
    elif a>=60 and a<=69:
        print("D")
    elif a>=50 and a<=59:
        print("E")
    else:
        print("F")
        
    