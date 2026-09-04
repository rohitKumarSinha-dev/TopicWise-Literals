# # # # #Example - Understanding the flow of While Loop

n = 5
while n > 0:
    print(n)
    n = n-1
else:
    print("n can not be greater than 0")

##--------------Logic Using While Loop------->
# #
# # # print("Logic Using While Loop")
n= 3
i = 0
while i < 10:
    i = i + 1
    print(n * i )
#
 #problem NO 3

n = 4356
while n > 0:
    r = n % 10
    print(r)
    n = n // 10
    print(n)
else:
    print("Exit the loop if its Come ZERO(0)")

# Problem No 4 ---- Count the TOTAL digit
n = 373829
i = 0
while n > 0:
    i = i + 1
    n = n // 10
print('Number of Total Digit', i)

# # # # Problem 5-  Topic ----> Sum of digit of a Number
n = 373829
sum = 0
while n > 0:
    r = n % 10
    sum = sum + r
    n = n // 10
print("Sum of Digit", sum)

## Topic ------>Reversing A number  <----------------
# #
n = int(input("Enter a Number:"))
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print ("Reverse number is:", reverse)


# # ## Topic ------> PALINDROME (Reverse of a number and in result when it gets reversed it should give a same number )<----------------
#
n = int(input("Enter a number Palindrome/Not Palindrome:"))
orginal = n
reverse = 0
while n > 0 :
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
if orginal == reverse:
        print ("Reverse number is:", reverse)
else:
        print ("It is not a Palindrome")

## -----> Summation Logic using WHILE LOOP Condition<--------

n = 5
i = 0
Sum = 0
while i < n:
         i = i + 1
         Sum += i
print(Sum)

# ## -------------Summation Logic - PART 2 --------

m = 10
i = 100
Sum2 = 0
while i > m:
    Sum2 -= i
    i = i - 1
print(Sum2)

##Find the [Sum of n numbers] , Let's supose n = 5 .

numbers = [2, 5, 9, 6, 4]
n = len(numbers)
i = 0
All_Sum = 0
while i < n:
    All_Sum += numbers[i]
    i += 1
print(All_Sum)














