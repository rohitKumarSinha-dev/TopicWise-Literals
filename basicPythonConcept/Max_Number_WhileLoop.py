#Find the Max Element from this 5 numbers
#First method:-
numbers = [1, 10 , 22, 31, 10]
n = len(numbers)
i = 0
maximum = numbers[0]
while i < n:
    if numbers[i] > maximum:
        maximum = numbers[i]
    i += 1
print("Maximum Element:", maximum)

# 2nd Method :-
n = 5
print('Enter', n , 'numbers')
i = 0
Max = 0
while i < n:
    i += 1
    x = int(input(''))
    if x > Max:
        Max = x
print('Using 2nd Method(Taking input from keyboard)','Max element is ', Max)


