# calculator
from classWork.CalculatorTest import run_tests


def add(num1: float, num2: float) -> float:
    """a function that adds two numbers"""
    #     logic here
    num3 = num1 + num2
    return num3


def subtract(num1: float, num2: float) -> float:
    """a function that subtracts num2 from num1"""
    #     logic here
    num3 = num1 - num2
    return num3


def multiply(num1: float, num2: float) -> float:
    """a function that multiplies two numbers"""
    #     logic here
    num3 = num1 * num2
    return num3


def division(num1: float, num2: float) -> float:
    """a function that divides two numbers"""
    #     logic here
    num3 = num1 / num2
    return num3


def square_root(num1: float) -> float:
    """a function that returns the square root of number"""
    #     logic here
    num2 = num1 ** 0.5
    return num2


def square(num1: float) -> float:
    """a function that adds two numbers"""
    #     logic here
    num2 = num1 ** 2
    return num2


result = add(5, 2)
print(result)


def main():
    # run all the tests
    run_tests()

    # add 2 nums
    x = 2
    y = 10
    z = add(x, y)
    print(f"x + y: {x} + {y} = {z}")


if __name__ == "__main__":
    main()
