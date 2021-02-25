# # 2.1 (What does this code do?) Create the variables x = 2 and y = 3, then determine what
# # each of the following statements displays:
# x = 2
# y = 3
#
# # a)
# print('x =', x)
# # Answer x = 2
#
# # b)
# print('Value of', x, '+', x, 'is', (x + x))
# # Answer Value of 2 + 2 is 4
#
# # c)
# print('x =')
# # Answer x =
#
# # d)
# print((x + y), '=', (y + x))
# # Answer 5 = 5


# 2.2 (What’s wrong with this code?) The following code should read an integer into the
# variable rating:
# rating = input('Enter an integer rating between 1 and 10')
# input returns as a string, so the user would not be able to type in an input

# 2.3 (Fill in the missing code) Replace *** in the following code with a statement that
# will print a message like 'Congratulations! Your grade of 91 earns you an A in this
# course'. Your statement should print the value stored in the variable grade:
# if grade >= 90:
#  ***

# grade = 91
# if grade >= 90:
#     print('Congratulations! Your grade of', grade, 'earns you an A in this course')

# 2.4 (Arithmetic) For each of the arithmetic operators +, -, *, /, // and **, display the
# value of an expression with 27.5 as the left operand and 2 as the right operand.

# print(27.5 + 2)
# # Answer 29.5
#
# print(27.5 - 2)
# # Answer 25.5
#
# print(27.5 * 2)
# # Answer 55.0
#
# print(27.5 / 2)
# # Answer 13.75
#
# print(27.5 // 2)
# # Answer 13.0
#
# print(27.5 ** 2)
# # Answer 756.25


# 2.5 (Circle Area, Diameter and Circumference) For a circle of radius 2, display the diameter, circumference and area.
# Use the value 3.14159 for π. Use the following formulas
# (r is the radius): diameter = 2r, circumference = 2πr and area = πr2. [In a later chapter, we’ll
# introduce Python’s math module which contains a higher-precision representation of π.]

# pie = 3.14159
# print(pie)
# radius = 2 * pie
# print(radius)
# diameter = 2 * radius
# print(diameter)
# circumference = 2 * pie * radius
# print(circumference)
# area = pie * (radius ** 2)
# print(area)


# 2.6 (Odd or Even) Use if statements to determine whether an integer is odd or even.
# [Hint: Use the remainder operator. An even number is a multiple of 2. Any multiple of 2
# leaves a remainder of 0 when divided by 2.]

# number = (int(input("Enter an number:")))
# if number % 2 == 0:
#     print(number, "is an even number")
# else: print(number, "is an odd number")


# 2.7 (Multiples) Use if statements to determine whether 1024 is a multiple of 4 and
# whether 2 is a multiple of 10. (Hint: Use the remainder operator.)

# if 1024 % 4 == 0:
#     print("1024 is a multiple of 4")
# if 2 % 10 == 0:
#     print("2 is a multiple of 10")
# else: print("2 is not a multiple of 10")

# 2.8 (Table of Squares and Cubes) Write a script that calculates the squares and cubes
# of the numbers from 0 to 5. Print the resulting values in table format, as shown below. Use
# the tab escape sequence to achieve the three-column output.

# number square cube
# 0         0     0
# 1         1     1
# 2         4     8
# 3         9     27
# 4         16    64
# 5         25    125
# The next chapter shows how to “right align” numbers. You could try that as an extra challenge here.
# The output would be:
# number square cube
#  0 0 0
#  1 1 1
#  2 4 8
#  3 9 27
#  4 16 64
#  5 25 125


# 2.9 Display the integer equivalents of B C D b c d 0 1 2 $ * + and the space character.
# print(ord('B'))
# print(ord('C'))
# print(ord('D'))
# print(ord('b'))
# print(ord('c'))
# print(ord('d'))
# print(ord('0'))
# print(ord('1'))
# print(ord('2'))
# print(ord('$'))
# print(ord('*'))
# print(ord('+'))
# print(ord(' '))

# Answer
# 66
# 67
# 68
# 98
# 99
# 100
# 48
# 49
# 50
# 36
# 42
# 43
# 32


# 2.10 (Arithmetic, Smallest and Largest) Write a script that inputs three integers from
# the user. Display the sum, average, product, smallest and largest of the numbers. Note that
# each of these is a reduction in functional-style programming.



