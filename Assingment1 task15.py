a=float(input())
b=int(input())
if b<30 or a<3.80:
    print("The student is not eligible for a waiver")
else:
    if a>=3.80 and a<=3.89:
        print("The student is eligible for a waiver of 25 percent.")
    elif a>=3.90 and a<=3.94:
        print("The student is eligible for a waiver of 50 percent.")
    elif a>=3.95 and a<=3.99:
        print("The student is eligible for a waiver of 75 percent.")
    else:
        print("The student is eligible for a waiver of 100 percent.")