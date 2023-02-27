"""
Write the Python code of a program that reads two numbers from the user. 
The program should then print "First is greater" if the first number is 
greater, "Second is greater" if the second number is greater, and 
"The numbers are equal" otherwise.
"""
a=int(input())
b=int(input())
if a>b:
    print("First is greater")
elif b>a:
    print("Second is greater")
else:
    print("The numbers are equal")