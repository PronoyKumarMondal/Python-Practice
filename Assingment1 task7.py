"""Write the Python code of a program that reads an integer, 
and prints the integer it is a multiple of either 2 or 5 but not both.
If the number is a multiple of 2 and 5 both, then print "Multiple of 2 and
5 both". For all other numbers, the program prints "Not a multiple we want"."""

a=int(input())
if a%2==0 and a%5==0:
    print("Multiple of 2 and 5 both")
elif a%2==0 or a%5==0:
    print(a)
else:
    print("Not a multiple we want")