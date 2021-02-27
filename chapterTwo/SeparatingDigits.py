# 2.11 ( (Separating the Digits in an Integer) Write a script that inputs a five-digit integer
# from the user. Separate the number into its individual digits. Print them separated by three
# spaces each. For example, if the user types in the number 42339, the script should print


digit = 45678
print(digit)


# int(input("Enter five Digits:"))
def separating_first_digit(num: int) -> int:
    first_digit = num // 10000
    print(first_digit)

def separating_second_digit(num: int) -> int:
    secondMod = digit % 10000
    print(secondMod)

secondDigit = secondMod // 1000
print(secondDigit)

thirdMod = secondMod % 1000
print(thirdMod)

thirdDigit = thirdMod // 100
print(thirdDigit)

fourthMod = thirdMod % 100
print(fourthMod)

fourthDigit = fourthMod // 10
print(fourthDigit)

fifthMod = fourthMod % 10
print(fifthMod)

# int((print(firstDigit +' '+ secondDigit + '    '  + thirdDigit + '   '+ fifthMod )))
