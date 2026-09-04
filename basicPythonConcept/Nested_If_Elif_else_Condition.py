# QA 1 - Given a day number as input, output the corresponding day name.
dayNo = int(input("Enter a DAY Number: "))

if dayNo == 0:
    print("Monday")
elif dayNo == 1:
    print("Tuesday")
elif dayNo == 2:
    print("Wednesday")
elif dayNo == 3:
    print("Thursday")
elif dayNo == 4:
    print("Friday")
elif dayNo == 5:
    print("Saturday")
elif dayNo == 6:
    print("Sunday")
else:
    print("Invalid input. Please enter a numeric value.")

# Q2 - Given a Month number as input, output the corresponding Month name.

monthNo = int(input("Enter a Month Number: "))
if monthNo == 0:
    print("January")
elif monthNo == 1:
    print("February")
elif monthNo == 2:
    print("March")
elif monthNo == 3:
    print("April")
elif monthNo == 4:
    print("May")
elif monthNo == 5:
    print("June")
elif monthNo == 6:
    print("July")
elif monthNo == 7:
    print("August")
elif monthNo == 8:
    print("September")
elif monthNo == 9:
    print("October")
elif monthNo == 10:
    print("November")
elif monthNo == 11:
    print("December")
else:
    print("Invalid input. Please enter a correct numeric value.")

