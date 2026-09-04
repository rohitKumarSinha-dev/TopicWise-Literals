## In Python , Chaining Comparison Operator means you can write multiple comparison in a single
# concise expression, similar to mathematical notation.

x = 21
start = 10
end = 20
# Traditional Way
if x >= start and x <= end:
    print("x is within the range")
# Simplified CHAINED Comparison
if start <= x <= end:
    print("x is within the range")
else:
    print("x is not within the range")


## 2nd topic [Is and Is not ] or is and is not
# Here (is) refer to SAME DATA.
a = 10
b = a
if (b is a):
    print("b is a")

# Example 2 - if both the value is same for different variable
x = 25
y = 25
# Here it is refering to same literals,(value of y is refering to variable x, Its is not creating any new memory for that)


