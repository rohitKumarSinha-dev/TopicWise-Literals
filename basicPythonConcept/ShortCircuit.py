# -> We will revisit the Logical Operator
##-> Then we will look what is mean by short circuit
# --> {This [Short Circuit] work on "and" operator , "or" operator}

#-> And we will see What is "Non - Boolean Condition"

# So , First -
## Logical Operator which - RETURNS [True/False]
## [ and , or , not ]
## [AND , OR , NOT]

## Start with { Short Circuit with "and" }
### - In this condition it will check only the first condition
# ----> Using of Compound Conditional Statement
### ----, Below Example 1.., what happened only the condition of value "a" is compared all possibilities
a = 3.0182
b = 5
c = 8
if a < b and a < c:
    print("a is smaller than both b and c")
elif a > b and a > c:
    print("a is greater than both b and c")
elif a < b and a > c:
    print("a is less than b but greater than c")
else:
    print("a is greater than b but less than c")

## 2 - SHORT CIRCUIT with "or" operator
a = 3.0182
b = 5
c = 8
if a != b or a != c:
    print("a != b and a != c",a != b or a != c)
elif a > b and a < c:
    print("A is not greater than b- a > b and A is not greater than c-  a > c",
          a > b and a < c )
elif a < b and a < c:
    print("a is smaller b and c ", a < b and a < c)
elif b > c and c > a:
    print("b is greater than c",b > c and c > a )
else:
    print("a is smaller and b and c is greater b and a ")


 ### Example 3 -

a = 4.0182
b = 0.5
c = 8.001

if a != b and a != c:
    print("a is different from both b and c")

if a > b and a < c:
    print("a is greater than b and less than c")

if a < b and a < c:
    print("a is smaller than both b and c")

if b > c and c > a:
    print("b is greater than c and c is greater than a")

if a > b and a > c:
    print("a is greater than both b and c")


# Non Boolean Condition
# False --> 0
# True --> any other value is true here  eg., [1 , -1, 10 , -15, 7]

# So its means that BOOLEAN number can be related with the integer value.

# So now check ---> What is Non-Boolean Condition is --->
# example - if 5 and 10 (means if 5 is true and 10 is also true then the result whould be TRUE)_ Ans 10
# 5(T) and 0(F) --> 0 (Because in and condition , it check the second last condition)
# 0(F) and 10(T) --> O(F) - in and if first condition is False then the result is False


# Lets Jump into (or) condition
#If both are true in OR condition it should
# check the first condition
# 5(T) or 10(T) --> 5(T)

#IF the first condition is False
# then it should check the second condition
# --> 0(F) or 10(T) --> 10(True)


a = 10
format(a,'b')
print(format(a,'b'))