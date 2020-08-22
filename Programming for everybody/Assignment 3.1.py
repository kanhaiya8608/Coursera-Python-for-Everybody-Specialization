"""
3.1 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. Pay the hourly rate for the hours up 
to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay
should be 498.75).
"""
hrs = input("Enter hours:")
h = float(hrs)

rte = input("Enter rate:")
rate = float(rte)

if h <= 40:
    pay = h * rate
elif h > 40:
    pay = 40*rate + (h-40)*rate*1.5

print(pay)
