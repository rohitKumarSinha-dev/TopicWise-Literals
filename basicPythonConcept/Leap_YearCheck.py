# Check whether Year is LEAP YEAR OR NOT
CheckLeapYear = int(input("Enter a Year:"))
if (CheckLeapYear % 4 == 0 and
        CheckLeapYear % 100 != 0
        or CheckLeapYear % 400 == 0):
    print("leap year")
else:
    print("not a leap year")
