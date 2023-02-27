"""
Write a Python program to compute and display a person’s weekly salary as determined by the following conditions:
●	If the hours worked is less than or equal to 40, then the person receives Tk 200 per hour.
●	If the hours worked is greater than 40, then the person receives Tk 8000 plus Tk 300 for each hour worked over 40 hours.
The program should request the hours worked as an input from the user and display the salary as output. You need to make sure that user input is valid. For example, a person cannot work for -5 hours or more than 168 hours in a week. So, the valid hours range is 0 to 168. For invalid hours, print outputs as given in the samples below.
"""
h = int(input())
b = 0
if h < 0:
    print("Hour cannot be negative")
else:
    if h > 40:
         b = h-40
         h=40
    print((h*200)+(b*300))
