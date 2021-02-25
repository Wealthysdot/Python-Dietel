num1 = (int(input("Enter first number:")))
num2 = (int(input("Enter second number:")))
num3 = (int(input("Enter third number:")))


def add(num1: float, num2: float, num3: float) -> float:
    """a function that adds three numbers"""
    #     logic here
    addition = num1 + num2 + num3
    return addition


def avg(num1: float, num2: float, num3: float) -> float:
    """a function that calculates the average of  three numbers numbers"""
    #     logic here
    average = add(num1, num2, num3) / 3
    return average


def prd(num1: float, num2: float, num3: float) -> float:
    """a function that calculates the product of  three numbers numbers"""
    #     logic here
    product = num1 * num2 * num3
    return product


smallest = num1
largest = num1
if smallest >= num2:
    smallest = num2
elif largest <= num2:
    largest = num3
if smallest >= num3:
    smallest = num3
elif largest <= num3:
    largest = num3

print("Product:", prd(num1, num2, num3))
print("Average: ", avg(num1, num2, num3))
print("Addition: ", add(num1, num2, num3))
print("Smallest is ", smallest)
print("Largest is ", largest)