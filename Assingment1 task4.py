"""
Write the Python code of a program that reads two numbers, subtracts the 
smaller number from the larger one, and prints the result.
"""
a=int(input())
b=int(input())
if (b>a):
    temp=a
    a=b
    b=temp
print(a-b)