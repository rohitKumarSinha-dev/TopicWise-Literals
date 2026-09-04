# Starting with Contional - Relational Operators
"""
It inculde operators like and used it is to COMPARE THE DATA --->
< - less than
<= - less than equal to
> - greater than
>= - greater than equal to
== - equal  (like we do in maths a1 = a2 so here == is woring as equal to sign)
!= - not Equal to

--> here result comes in the form of Boolean Value like True/False
"""

"""
4 < 5 --Value Comes as--> True 
4 <= 5 --Value Comes as--> True 
4 > 5 --Value Comes as--> False
4 >= 5 --Value Comes as--> False
4 == 5 --Value Comes as--> False
4 != 5 --Value Comes as--> True  
"""

#  Conditional Statements
#  ALSO checking/Adding with Relational Operators , because without this
#  you can't access or perform Condtional Statement
"""
There are 3 type of conditional statements --->>
1- if <condition> :
2 - else: 
3 - elif <condition>: 
"""
# print("==========1st Approch where staic value as 10 for a to check==============")
#  QUESTION - CHECK A NUMBER IS POSITIVE OR NEGATIVE using Conditional Statement
# So here we basically taken a staic value as 10 for a to check what value it should return
# a = 10
# if a >= 10:
#     print('Positive Value')
# else:
#     print('Negative Value')

# print("==========2nd Approch where take value from user input to check==============")
# 2nd Approch -> So here we basically taken a user input value to check what value it should return

# def check_number(num):
#     if num > 0:
#         return "positive Number"
#     elif num < 0:
#         return "Negative Value "
#     else:
#         return "Zero"
# # Taking input from user
# number = float(input("Enter a number:"))
# # Function call
# result = check_number(number)
# # Output
# print(result)
#
# print("==========3rd Approch - Applying condition that accept number only based on input user value==============")
# def classify_value(num):
#     if num > 0:
#         return "positive Number"
#     elif num < 0:
#         return "Negative Value "
#     else:
#         return "Zero"
#
# def read_numeric_input():
#     while True:
#         try:
#             raw_data = input("Enter a numberic Value:")
#             converted_value = float(raw_data)
#             return converted_value
#         except ValueError:
#             print("Invallid input, Please Enter Number Only.")
# user_value = read_numeric_input()
# classification = classify_value(user_value)
# print(classification)

"""
COMPOUND CONDITIONAL STATEMENTS -
1 - LOGICAL OPERATORS 
2 - COMPOUND CONDITIONAL STATEMENTS
3 - TRUTH TABLE 
EXAMPLE  
"""
"""
1 - logical operator - is small case (and ,or, not) , in caps case (AND ,OR, NOT)
it gives boolean result in form of True or False
"""
"""
2 - COMPOUND CONDITIONAL STATEMENTS- 
Here we are just reveising the concept , to write and understand how to use compound conditional statements.
first we have to reveise some things like conditional statement 
the syntax is below - 
    if<condition>:
        ------------
        ------------
        ------------
    else:
        ------------
        ------------
For writing above conditional statement we have to use Relational Operators like 
[< , >, <=, >=, ==, !=]
to understand this let's take an example
        ---by the help of logical operator ,(AND ,OR, NOT)-they help us to combine two condition.
 a = 10 
 b = 6
 c = 9
  if<condition1> and <condition2>>:
        ------------
        ------------
        ------------
    else:
        ------------
        ------------
        
a>b  |  a>c  |  (a>b) AND (a>c) | (a>b) OR (a>c)
------------------------------------------------
True   True        True               True

Let Suppose:
    P = (a > b)
    Q = (a > c)

P      Q      P AND Q  |  P OR Q
--------------------------------
True   True     True   |   True
True   False    False  |   True
False  True     False  |   True
False  False    False  |   False

AND means always false , if it will be true , when all are true .

2 - Now , check with OR operator , IT - [Returns True if at least one condition is True.]
Let Suppose:
a = 10
b = 6
c = 9
    P = (a > b)
    Q = (a > c)
    
    (a > b) or (a>c)
 if<condition1> or <condition2>>:
        ------------
        ------------
        ------------
    else:
        ------------
        ------------
P      Q      P OR Q
----------------------
True   True     True
True   False    True
False  True     True
False  False    False

3 - Now, check NOT Condition Truth Table, [NOT simply reverses the result]
a = 10
b = 6
c = 9
  :- NOT Condition Truth Table
------------------------with b comparison
a>b    NOT(a>b)
-----------------
True     False
------------------------with c comparison
a>c    NOT(a>c)
-----------------
True     False

P = (a > b) → True
Q = (a > c) → True

P      NOT P
-------------
True   False
False  True

//- NOT simply reverses the result

True → False
False → True
"""
#
# """
# 1. and → All conditions must be TRUE
# """
# print("-----[1. and → All conditions must be TRUE]-------")
# age = int(input("Enter your age: "))
# has_id = True
#
# if age>=18 and has_id:
#     print("Age is Accepeted as per criteria")
# else:
#     print("Age is not accepted as per criteria")
#
# print("--------------------------------------1.1-----------------------------------------------------------")
# """
# Question1.1 - A user can access premium content only if:
# age ≥ 18
# AND user has an active subscription
# """
# print("-----Practise Question 1.1 - access premium content only if:age ≥ 18-------------")
# def canAccess_subscription_isActive(age, has_subscription):
#     if age>=18 and has_subscription:
#         return"Access Granted"
#     return "Access Denied"
# age = (int(input("Enter your Age:")))
# subscription_input = input("Do you have active subscription ?(yes/no):")
# has_subscription = subscription_input.lower() == "yes"
# print(canAccess_subscription_isActive(age,has_subscription))
#
# print("-----------------------------------------2--------------------------------------------------------")
#
# print("-----Practise Question 2 - Give discount over payment of more than $1000-------------")
# """
# Question 2 - Give discount if:
# purchase amount ≥ 1000
# OR user is a premium member
# """
# def check_discount(purchase_amount, is_premium):
#     if purchase_amount >= 1000 or is_premium:
#         return "Discount Applied"
#     return "No Discount"
# amount = float(input("Enter your purchase amount: "))
# is_premium = input("Premium User?(yes/no):" ).lower() == "yes"
# print(check_discount(amount,is_premium))
# # 218 - logic alternative  to handle case sentitivity for (yes/no)
# # user_input = input("Premium user? (yes/no): ")
# # lower_value = user_input.lower()
# #
# # if lower_value == "yes":
# #     is_premium = True
# # else:
# #     is_premium = False
# print("--------------------------------------------3-----------------------------------------------------")
#
# print("-----Question 3 - Login Security Check-------------")
# """
# Question 3 - Login Security
# Allow login only if:
#     username matches
#     AND password matches
#     AND account is NOT locked/Active Users
# """
# def authenticate(username, password, locked):
#     if username == "rohit" and password == "Test@124" and not locked:
#         return "Login Successful"
#     return "Login Failed"
# age = int(input("Enter your age: "))
# subscription_input = input("Do you have an active subscription? (yes/no): ")
# has_subscription = subscription_input.lower() == "yes"
# print(canAccess_subscription_isActive(age, has_subscription))

print("--------------------------------------------4-----------------------------------------------------")

print("---------- Q4. Range Validation-------------")
"""
Question 4. Range Validation 
Check if a number lies between 10 and 50 (inclusive)
"""

def in_range(number ):
    "Check if number is between 10 and 50"
    if number < 0 :
        return "Negative No.is not allowed , only number lies between 10 to 50 has to be entered "
    if number >= 10 and number <= 50:
        return "Number is in RANGE"
    else:
        return "Number is not in Range"
try:
    number = float(input("Enter any number (decimals allowed): "))
    print(in_range(number))
except ValueError:
    print("Invalid input. Please enter a numeric value.")


