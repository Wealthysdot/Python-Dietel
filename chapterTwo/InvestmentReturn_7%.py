# 2.12 (7% Investment Return) Some investment advisors say that it’s reasonable to expect a 7% return over
# the long term in the stock market. Assuming that you begin with
# $1000 and leave your money invested, calculate and display how much money you’ll have
# after 10, 20 and 30 years. Use the following formula for determining these amounts:
# a = p(1 + r)**n
# where
# p is the original amount invested (i.e., the principal of $1000),
# r is the annual rate of return (7%),
# n is the number of years (10, 20 or 30) and
# a is the amount on deposit at the end of the nth year.

# n = int(input("Enter the number of years of investment:"))
# p = 1000


# r = 0.84

def calculate_r(n1: float, n2: float, n3: float) -> float:
    """A function that calculates the 7% annual rate of return)"""
    r = ((7 * 12) / 100)
    return r
    print(calculate_r(n1, n2, n3))


# a = (p * (1 + calculate_p()) ** n

# print(a)