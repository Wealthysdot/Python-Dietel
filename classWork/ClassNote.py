# # ways to write list
# #1. list =list()
# #2. names = []
# names = ['john', 'carol', 'kenny']
# print(names)
#
# # names.append("Odun")
# # print(names)
#
#
# names1 = ['john', 'carol', 'kenny']
# names2 = ['ade', 'ola', 'mofe']
# names3 = names1 + names2
# print(names3)
#
# #joining
# names_joined = "-".join(names1)
# print(names_joined)
#
# names_joined = "*".join(names1)
# print(names_joined)
#
#
#
# another_list = []
# list_of_numbers = [1,2,3,4]
# print(list_of_numbers)
#
# set_list_of_numbers = set(list_of_numbers)
# print (set_list_of_numbers )
#
#
# #adding to the list
# list_of_numbers.append(5)
# print(list_of_numbers)
#
# list_of_numbers.remove(2)
# print(list_of_numbers)
#
# removes with index address
# list_of_numbers.pop()
# print(list_of_numbers)
#
# #changing the element in the array
# # list_of_numbers[0] = 99
# # print(list_of_numbers)
#
# #adding number to a specific element of an array
# list_of_numbers[0] += 1
# print(list_of_numbers)
#
# #adding more number to the list
# list_of_numbers += [6]
# print(list_of_numbers)
#
# # # a string object is immutable, but a string in a list can be reassigned
# # # like saying
# # name = 'christian'
# # # and u want to change the c to z, it wont work except you say
# # new_name = name.replace("c", "z")
# # # trying to replace the c to z, doesnt actually mean you are replacing the letters, you are actually creating
# # # a new object, because if we print the id of both objects name and new_name they are not the same
# # print(name)
# # # If you print name , the result would be christian,
# # print(id(name))
# # # meanwhile the id would be different from new_name and
# # print(new_name)
# # # if you print new_name this would result to zhristian
# # print(id(new_name))
#
#
# # # but you can replace the item on the list with another one
# # names[0] = 'remi'
# # print(names)
# # # we get result has ['remi', 'carol', 'kenny']
# # # you can also replace a letter in an item
# # names[0] = names[0].replace('r', 't')
# # print(names)
# # # This command replaces the last element on the list, even if you dont know the amount of items on the list
# # names[-1] = True
# # print(names)
#
#
# # ages = [23, 45, 32]
# # ages[0] = 'peter'
# # print(ages)
# # # you use this function to get the 'type' of the element in the list
# # # typelist = lambda li: [type(x) for x in li]
# # # print(typelist(ages))
# # # using the list command break the element into separate letters
# # print(list(ages[0]))
# #
# # # the result ['p', 'e', 't', 'e', 'r']
# # # split command sort of like eliminates the letter in the parenthesis
# # print(ages[0].split("e"))
# # # ['p', 't', 'r']
# #
# # # a, b, c, d = 'he', 'is', 'a', 'boy'
# # # print('{:<3}{:<4}{:<4}'.format(a, b, c, d))
#
#
# # # list and join
# # li = "123.456.789"
# # a = li.split(".")
# # print(a)
# # print("".join(a))
#
# Tuple are simply immutable list, they are recognized with a comma
# (mile, fuel) = (input("mile, fuel: ").split(","))
# you have to individually cast the type after spliting, because splitting provides a list
# mile = int(mile)
# fuel = int(fuel)
# print("mile", mile)
# print("fuel", fuel)
# trip = (mile / fuel)
# print(trip)
#
#  casting to tuple
# tuple_list_of_numbers = tuple(list_of_numbers)
# print(tuple_list_of_numbers)
#
#
# # append, extend, and del make list mutate but does not work on tuple
#  append provides value
# extend and concatenate are similar
# # python dictionary
# # {} is used to create a a dictionary
# # you use the: marker to indicate key:value pairs
# # the keys are immutable
# # dictionary can be mutable
# # it does not respect orders
# # key cannot be a list
# # contact = {'bill': '354545', 'rich': '4646', }
# # print(contact)
# # print(contact["bill"])
#
#
#
# # # Set
# # is a list that only contains unique elements
# # it does not have keys
# # it can only contain immutable types


# Selection
# this is how programs make choice, to know what exactly they are doing at a break
# if boolean expression:
#     suite
# number = 3
# (enter) = (int(input("A number:")))
# if enter >= number:
#     print(enter, "is greater than", number)
# else:
#     print(enter, "is lesser than", number)

# while loop is dependent on the condition
# while boolean expression:
#     suite


# for loop
# in important you have a collection, create a list
# for element in collection:
#     suite

# num=[1,2,3,4]
# for spongebob in num:
#     print(spongebob)

# num = "hello"
# for spongebob in num:
#     print(spongebob)
#



# for shakiti, bobo in enumerate(num):
#     print(shakiti, bobo)


# **reade about range in python
# for i in range(0, 20, 2):
#     print(i)


# Boolean expression
# they evaluate to true and false
# empty object are seen as false int-0, string-"", empty[]
# True is any object that is non-empty or non-zero.

# None - a

# relational operator

# Equality
# == check if they rep the same value

# is is a key word to know if they are associated with the same value


# chained comparisons
# and (like in java  &&)


# boolean operator
# and case gives false
# or gives the true


# FUNCTION
# function is the way of encapsulating logic
# reoccurence  is only for a value
# classes get to rep both classes and object

#
# def keyword, function_name, (parameter, parameter1):
#     statement1
#     statement2
# return value_to_return(optional, but would return null, if not indicate)
#

# Annotation(type annotation)
# hinting the type of your work
# def multiply(num1: float, num2:float)->float:


# .find is used to search for
#
# chaining methods
# putting method in method

# optional arguments
# s.find(sub[, start [end]]
# the start and finish is optional, if u dont provide it it would assume that from begining to the ens
# consider space character in quotes


# nesting methods
# making the result of one method as an argument to another
# a_str.find('t', a_str.find('t')+1)
# this is used to find a second t in a word/sentence
# the +1 is like telling it to continue from where the initial search stopped without going to start from the begining

#   Each format string
# {:alighn witdth.precision descriptor}
# :align is optiona(default left)
# width how many space in word(default let)(if u say 10 with and u have 4words, it would give 6, cos it contains the word given too)
# precision is for floating point rounding(default no rounding)
# type is hte expected type(error if the arg is the wrong type)
# print{:>10s.format billy}
# string formatting can be used to create table


# String iteration
# -for loop
# -enumerate
# -palindrome(case does not matter, punction is ignored)
# s="hello"
# s[::-1]
# s==s[::-1]
# would return false
# -split

# sign + or -
# a = 100
# b = -20
# using + (using + tells it to show the sign in fron to the digit)
# print("a = {0:+}, b={1:+}".format(a, b))
# result shows a = +100, b=-20
# using -(shows only the negative line)
# print("a = {0:-}, b={1:-}".format(a, b))
# result a = 100, b=-20


# x = 6535671731981800994
# print("{0:,d}".format(x))
# result shows - 6,535,671,731,981,800,994 putting commas in the number

# s = "Johnny"
# print("{0:*>50s}".format(s))
# return ********************************************Johnny has result

# Recursion is when a function calls itself
# made up of a selection function(base case) and the function itself

# Fibonacci
# a sequence that is created by the sum of thr last two value

# bottle, book, pen, mouse, pendant  