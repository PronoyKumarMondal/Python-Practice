n=input()
l=len(n)
if l<4:
   print(n)
elif l>3:
         if n[-1]=="r" and n[-2]=="e":
             i=0
             for i in range(l-1):
                 if i==l-1 or i==l-2:
                     continue
                 else:
                     print(n[i],end="")
             print("est")
         elif n[-1]=="t" and n[-2]=="s" and n[-3]=="e":
            print(n)
         else:
             print(n,end="")
             print("er")