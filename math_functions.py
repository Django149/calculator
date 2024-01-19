import math


def add(x: int | float, y: int | float) -> int | float:
    """
    Adds two numbers
    :param x: First number
    :param y: Second number
    :return: Sum of x and y
    """
    return x + y


def subtract(x: int | float, y: int | float) -> int | float:
    """
    Subtracts two numbers
    :param x: First number
    :param y: Second number
    :return: Difference of x and y
    """
    return x - y


def multiply(x: int | float, y: int | float) -> int | float:
    """
    Multiplies two numbers
    :param x: First number
    :param y: Second number
    :return: Product of x and y
    """
    return x * y


def divide(x: int | float, y: int | float) -> float:
    """
    Divides two numbers
    :param x: Numerator
    :param y: Denominator
    :return: Quotient of x and y
    :raises ZeroDivisionError: If 'y' is zero
    """
    try:
        return x / y
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero")


def power(x: int | float, y: int | float) -> float:
    """
    Calculates x raised to the power of y.
    :param x: Base
    :param y: Exponent
    :return: x raised to the power of y
    :raises ValueError: If a negative number is raised to a fractional power
    """
    try:
        return math.pow(x, y)
    except ValueError:
        raise ValueError("Cannot raise a negative number to a fractional power")


def modulus(x: int | float, y: int | float) -> float:
    """
    Calculates the modulus of two numbers
    :param x: First number
    :param y: Second number
    :return: Remainder of x divided by y
    :raises ZeroDivisionError: If 'y' is zero
    """
    try:
        return x % y
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot modulo by zero")


def average(x: int | float, y: int | float) -> float:
    """
    Calculates the average of two numbers
    :param x: First number
    :param y: Second number
    :return: Average of x and y
    """
    return (x + y) / 2


def maximum(x: int | float, y: int | float) -> int | float:
    """
    Finds the maximum of two numbers
    :param x: First number
    :param y: Second number
    :return: Maximum of x and y
    """
    if x > y:
        return x
    return y


def minimum(x: int | float, y: int | float) -> int | float:
    """
    Finds the minimum of two numbers
    :param x: First number
    :param y: Second number
    :return: Minimum of x and y
    """
    if x < y:
        return x
    return y


def negate(x: int | float) -> int | float:
    """
    Negates a number
    :param x: Number to be negated
    :return: Negative of x
    """
    return -x


def factorial(x: int) -> int:
    """
    Calculates the factorial of a number
    :param x: Number to find the factorial of
    :return: Factorial of x
    :raises TypeError: If 'x' is not an integer
    :raises ValueError: If 'x' is negative
    """
    if not isinstance(x, int):
        raise TypeError("Factorial is defined only for integers")
    if x < 0:
        raise ValueError("Factorial is not defined for negative values")
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result


def sum_of_digits(x: int | float) -> int:
    """
    Calculates the sum of the digits of a number
    :param x: Number to find the sum of digits
    :return: Sum of the digits of the number
    :raises ValueError: If 'x' is not positive
    """
    if x <= 0:
        raise ValueError("'#' operator is defined only for positive values")
    if isinstance(x, float):
        x_without_point = str(x).replace('.', '')
        x = int(x_without_point)
    digits_sum = 0
    while x != 0:
        digits_sum += x % 10
        x //= 10
    return digits_sum
