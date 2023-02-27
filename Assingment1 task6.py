"""
Write the Python code of a program that reads an integer as input from 
the user, and prints the integer if it is a multiple of 2 OR 5 and prints 
"Not a multiple of 2 OR 5" otherwise.
"""
a=int(input())
if a%2==0 or a%5==0 :
    print(a)
else:
    print("Not a multiple of 2 OR 5")