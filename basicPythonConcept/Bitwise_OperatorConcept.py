# #Topic --> Bitwise-Operator
# # What is Bitwise Operator
# # List of Bitwise Operator
#
# #In Python, a bitwise operator is used to perform operations directly on the binary (bit-level) representation of integers.
# #These operators treat numbers as sequences of bits (0 and 1) and manipulate them accordingly.
#
# #Common Bitwise Operators in Python
# #Operator	Name	Description	Example (a=5, b=3)
# # (&)	AND	-> Sets each bit to 1 if both bits are 1.	5 & 3 → 1 (0101 & 0011 = 0001)
# # (|)	|	OR -> Sets each bit to 1 if at least one bit is 1.
# # (^)	XOR ->	Sets each bit to 1 if only one bit is 1.	5 ^ 3 → 6 (0101 ^ 0011 = 0110)
# # (~)	NOT	 -> Inverts all bits (two’s complement form).	~5 → -6
# # (<<)	Left Shift -> Shifts bits to the left, filling with 0s.	5 << 1 → 10 (0101 → 1010)
# # (>>)	Right Shift	Shifts bits to the right, discarding shifted bits.	5 >> 1 → 2 (0101 → 0010)
#
# ## Example in Python
#
# # Example values
# a = 5   # binary: 0101
# b = 3   # binary: 0011
#
# print("a & b =", a & b)   # AND
# print("a | b =", a | b)   # OR
# print("a ^ b =", a ^ b)   # XOR
# print("~a =", ~a)         # NOT
# print("a << 1 =", a << 1) # Left shift
# print("a >> 1 =", a >> 1) # Right shift
# # Output:
# #
# #
# # Copy code
# # a & b = 1
# # a | b = 7
# # a ^ b = 6
# # ~a = -6
# # a << 1 = 10
# # a >> 1 = 2
# # ✅ Key Points:
# #
# # Bitwise operators only work on integers in Python.
# # They are often used in low-level programming, masking, encryption, compression, and hardware control.
# # Negative numbers use two’s complement representation internally.
#
# # to check the bitwise number use a FUNCTION [format(a,'b')]
#
# a = 162
# format(a,'b') # format(a,'b')
# print(format(a,'b')) #--->10100010
#
# a = 162
# bin(a) #0b10100010
# print(bin(a)) # It should give the literals(binary literal string)
#
#
# # So what makes it different ->
# # Between format function and Binary Function
#
# # --------------------Bitwise Operation -------->

# 1 ---> And Operator - (It is the sign of Multiplication)
# 2 ---> OR Operator - (It is the sign of Addition)

# Example Checking All Operator -- >>>>
# print(10&13)
# print(format(10&13,'b')) # here what i am missing previously is [format(number) without a format
# # specification does not convert the number to binary.]
#
# print(10|13)
# print(format(10|13,'b'))
#
# print(10^13) #Xor
# print(format(10^13,'b'))
#
# print(~13)
# print(format(~13,'b'))

#Right Shift Concept (>>)
print(20 >> 1) #Shifting Right by 1 position
print(format(10,'b'))
print(20 >> 2) #Shifting Right by 2 position
print(format(5,'b'))

# Left Shift Concept (<<)
print (20 << 1) #Shifting Left by 1 position
print(format(40,'b'))