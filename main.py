from errors import InvalidNumberFormatError, InsufficientOperandsError, UnknownCharacterError, \
    InsufficientOperatorsError, InvalidUseOfOperatorError
from operators import BinaryOperator, RightUnaryOperator, LeftUnaryOperator, UnaryOperator
from math_functions import *

OPERATORS = {"+": BinaryOperator(1, add), "-": BinaryOperator(1, subtract), "*": BinaryOperator(2, multiply),
             "/": BinaryOperator(2, divide), "^": BinaryOperator(3, power), "unaryMinus": LeftUnaryOperator(1, negate),
             "%": BinaryOperator(4, modulus),
             "@": BinaryOperator(5, average),
             "$": BinaryOperator(5, maximum), "&": BinaryOperator(5, minimum), "~": LeftUnaryOperator(6, negate),
             "!": RightUnaryOperator(6, factorial), "#": RightUnaryOperator(6, sum_of_digits),
             "numberMinus": LeftUnaryOperator(10, negate)}


def is_number(item: str | int | float) -> bool:
    """
    Checks if the item is a number (integer or float)
    :param item: The item to check
    :return: True if item is a number (integer or float), False otherwise
    """
    return isinstance(item, int) or isinstance(item, float)


def is_operator(item: str | int | float) -> bool:
    """
    Checks if the item is an operator
    :param item: The item to check
    :return: True if item is an operator, False otherwise
    """
    return item in OPERATORS


def is_unary_operator(item: str | int | float) -> bool:
    """
    Checks if the item is a unary operator
    :param item: The item to check
    :return: True if item is a unary operator, False otherwise
    """
    return is_operator(item) and isinstance(OPERATORS[item], UnaryOperator)


def is_right_unary_operator(item: str | int | float) -> bool:
    """
    Checks if the item is a right unary operator
    :param item: The item to check
    :return: True if item is a right unary operator, False otherwise
    """
    return is_operator(item) and isinstance(OPERATORS[item], RightUnaryOperator)


def is_left_unary_operator(item: str | int | float) -> bool:
    """
    Checks if the item is a left unary operator
    :param item: The item to check
    :return: True if item is a left unary operator, False otherwise
    """
    return is_operator(item) and isinstance(OPERATORS[item], LeftUnaryOperator)


def is_binary_operator(item: str | int | float) -> bool:
    """
    Checks if the item is a binary operator
    :param item: The item to check
    :return: True if item is a binary operator, False otherwise
    """
    return is_operator(item) and isinstance(OPERATORS[item], BinaryOperator)


def handle_right_parenthesis(operator_stack: list[str], operand_stack: list[int | float]):
    """
    Handles the expression between the recent left parenthesis and the current right parenthesis
    :param operand_stack: list of operands
    :param operator_stack: list of operators
    :raises InsufficientOperatorsError: If there are mismatched parentheses (can be raised from execute_operation)
    :raises InsufficientOperandsError: If the execute_operation function raises this exception
    :raises InvalidUseOfOperatorError: If the execute_operation function raises this exception
    """
    while operator_stack and operator_stack[-1] != '(':
        execute_operation(operand_stack, operator_stack)
    if not operator_stack:
        raise InsufficientOperatorsError("Mismatched parentheses")
    operator_stack.pop()


def execute_operation(operand_stack: list[int | float], operator_stack: list[str]):
    """
    Executes one unary operation or one binary operation and insert the result into the operand_stack
    :param operand_stack: list of operands
    :param operator_stack: list of operators
    :raises InsufficientOperandsError: If there are insufficient operands to perform a binary operation
    :raises InvalidUseOfOperatorError: If an operator is used incorrectly
    :raises InsufficientOperatorsError: If there are mismatched parentheses
    """
    operator = operator_stack.pop()
    if operator == '(':
        raise InsufficientOperatorsError("Mismatched parentheses")

    func = OPERATORS[operator].get_function()
    if is_unary_operator(operator):
        if not operand_stack:
            if is_right_unary_operator(operator):
                raise InvalidUseOfOperatorError(f"Invalid use of {operator} operator")
            if is_left_unary_operator(operator):
                return

        operand = operand_stack.pop()

        try:
            num = func(operand)
        except (ValueError, TypeError) as e:
            raise InvalidUseOfOperatorError(e)
        if isinstance(num, float) and num.is_integer():
            num = int(num)

        operand_stack.append(num)

    else:
        if len(operand_stack) < 2:
            if operator == "(":
                raise InsufficientOperatorsError("Mismatched parentheses")
            else:
                raise InsufficientOperandsError(f"Not enough operands for binary operation ('{operator}')")

        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()

        try:
            num = func(operand1, operand2)
        except ZeroDivisionError as e:
            raise InvalidUseOfOperatorError(e)

        if isinstance(num, float) and num.is_integer():
            num = int(num)

        operand_stack.append(num)


def handle_operator(operator_stack: list[str], operand_stack: list[int | float], operator: str,
                    previous: str | int | float):
    """
    Handles the current operator in the expression and updates the operator_stack
    :param operand_stack: list of operands
    :param operator_stack: list of operators
    :param operator: The operator to process
    :param previous: The last character or number handled
    :raises InvalidUseOfOperatorError: If an operator is used incorrectly or if the execute_operation function raises
    this exception
    :raises InsufficientOperandsError: If the execute_operation function raises this exception
    :raises InsufficientOperatorsError: If the execute_operation function raises this exception
    """
    if is_left_unary_operator(previous) and operator != '-' and operator_stack and operator_stack[-1] != "(" and \
            operator_stack[-1] != ")":
        raise InvalidUseOfOperatorError(f"Operator '{previous}' needs to be next to a number or parentheses")

    if operator == '-':
        if previous is None:
            operator = "unaryMinus"
        elif not is_right_unary_operator(previous) and not is_number(previous):
            if previous == "unaryMinus":
                operator = "unaryMinus"
            else:
                operator = "numberMinus"

    if is_right_unary_operator(operator) and not (is_number(previous) or is_right_unary_operator(previous)):
        raise InvalidUseOfOperatorError(f"Operator '{operator}' should be to the right of a number")

    if is_left_unary_operator(operator):
        if is_number(previous) or is_right_unary_operator(previous):
            raise InvalidUseOfOperatorError(f"Operator '{operator}' should be to the left of a number")
        operator_stack.append(operator)
        return

    while operator_stack and operator_stack[-1] != '(' and OPERATORS[operator_stack[-1]].get_precedence() >= \
            OPERATORS[operator].get_precedence():
        execute_operation(operand_stack, operator_stack)

    operator_stack.append(operator)


def get_number(expression: str, index: int) -> tuple[int, int]:
    """
    Finds the number in the index place in the expression
    :param expression: The expression to find the number in
    :param index: The index where the number is starts
    :return: A tuple containing the number and the index to proceed from
    :raises InvalidNumberFormatError: If the number contains more than one decimal point
    """
    number_ended = False
    dot_appeared = False
    number = expression[index]
    index += 1
    while index < len(expression) and not number_ended:
        char = expression[index]
        if char.isdigit():
            number += char
            index += 1
        elif char == '.':
            if dot_appeared:
                raise InvalidNumberFormatError("A number cannot contain more than one decimal point")
            number += '.'
            dot_appeared = True
            index += 1
        else:
            number_ended = True

    if dot_appeared:
        number = float(number)
        if number.is_integer():
            number = int(number)
    else:
        number = int(number)

    return number, index - 1


def handle_number(operand_stack: list[int | float], expression: str, index: int, previous: str | int | float) -> tuple[
    int, int]:
    """
    Finds the number in the index place in the expression and insert the result into the operand_stack
    :param operand_stack: list of operands
    :param expression: The expression to find the number in
    :param index: The index where the number starts
    :param previous: The last character or number handled
    :return: A tuple containing the number and the index to proceed from
    :raises InvalidNumberFormatError: if the get_number function raises this exception
    :raises InsufficientOperatorsError: if there are not enough operators for a binary operation
    """
    if is_number(previous) or is_right_unary_operator(previous):
        raise InsufficientOperatorsError("Not enough operators for a binary operation")
    number, index = get_number(expression, index)
    operand_stack.append(number)
    return number, index


def evaluate_expression(expression: str) -> int | float:
    """
    Evaluates the given expression
    :param expression: The expression to evaluate
    :return: The result of the expression
    :raises InvalidNumberFormatError: If the handle_number function raises this exception
    :raises UnknownCharacterError: If an invalid character is encountered in the expression
    :raises InsufficientOperandsError: If there are not enough operands in the expression or if the handle_operator
    function raises this exception
    :raises InsufficientOperatorsError: If the handle_number function raises this exception or if the handle_operator
    function raises this exception
    :raises InvalidUseOfOperatorError: If the handle_operator function raises this exception
    """
    operand_stack = []
    operator_stack = []
    index = 0
    previous = None
    while index < len(expression):
        char = expression[index]

        if char == ' ' or char == '\t':
            pass

        elif char.isdigit():
            number, index = handle_number(operand_stack, expression, index, previous)
            previous = number

        elif is_operator(char):
            handle_operator(operator_stack, operand_stack, char, previous)
            previous = operator_stack[-1]

        elif char == '(':
            operator_stack.append(char)

        elif char == ')':
            handle_right_parenthesis(operator_stack, operand_stack)

        else:
            raise UnknownCharacterError(f"Invalid character encountered: {char}")

        index += 1

    while operator_stack:
        execute_operation(operand_stack, operator_stack)

    if not operand_stack:
        raise InsufficientOperandsError("Insufficient operands in the expression")

    return operand_stack.pop()


def handle_expression(expression: str):
    """
    Handles a given expression
    :param expression: The expression to handle
    """
    try:
        print(evaluate_expression(expression))
    except (InsufficientOperandsError, InvalidNumberFormatError, UnknownCharacterError, InsufficientOperatorsError,
            InvalidUseOfOperatorError) as e:
        print(f"{e.__class__.__name__}: {e}")


def main():
    """
    Main function that gets and processes the user's input
    """
    while True:
        try:
            expression = input('Enter an expression: ')
        except EOFError as e:
            print(e)
            continue
        handle_expression(expression)


if __name__ == '__main__':
    main()
