# Finding Max and Min Number
# Coding Exercise:
#      Do not use keyboard input.
#      All variables and input data should be hardcoded; you may change values for testing.
#
# Problem Definition:
#     Given a hardcoded list of numbers, use a while loop to find the largest (max) and smallest (min) elements.
#     Do not use the built-in max() or min() functions.
#
# Statements to Solve:
#
# Set up tracking variables for max and min (already provided).
#
# Process each element of the list using a while loop.
#
# Update the max and min variables if a larger or smaller element is found.
#
# Input/Output:
#
# Input: The variable numbers is a hardcoded list of integers.
# n is the count of numbers to process.
#
# Output: Print the maximum and minimum values using the given format:
#
# Max Element: <maximum value>
# Min Element: <minimum value>


number = [12, 45, 7, 89, 23]
n = len(number)

i = 0
Max = float('-inf')
Min = float('inf')

while i < n:
    x = number[i]
    if x > Max:
        Max = x
    if x < Min:
        Min = x
    i = i + 1
print("Maximum Number:", Max)
print("Minimum Number:", Min)
