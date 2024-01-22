from calculator_core.calculator_errors.invalid_number_format_error import InvalidNumberFormatError
from calculator_core.calculator_errors.insufficient_operators_error import InsufficientOperatorsError
from calculator_core.calculator_errors.insufficient_operands_error import InsufficientOperandsError
from calculator_core.calculator_errors.unknown_character_error import UnknownCharacterError

from operators.operator_errors.invalid_use_of_operator_error import InvalidUseOfOperatorError
from operators.operator_errors.invalid_value_for_operator_error import InvalidValueForOperatorError

from operators.operator_implementations.unary_operators.left_unary_operator import LeftUnaryOperator
from operators.operator_implementations.unary_operators.right_unary_operator import RightUnaryOperator

from operators.operator_types.binary_operator import BinaryOperator
from operators.operator_types.unary_operator import UnaryOperator

from operators.operators_dict import OPERATORS


def is_top_left_parenthesis(operator_stack: list[str]):
    """
    Checks if the top of the stack is a left parenthesis
    :param operator_stack: list of operators
    :return: True if the top of the stack is a left parenthesis, False otherwise
    """
    return operator_stack and operator_stack[-1] == "("


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


def handle_right_parenthesis(operator_stack: list[str], operand_stack: list[int | float],
                             is_previous_left_parenthesis: bool):
    """
    Handles the expression between the recent left parenthesis and the current right parenthesis
    :param operand_stack: list of operands
    :param operator_stack: list of operators
    :param is_previous_left_parenthesis: A boolean indicating if the previous character is a left parenthesis
    :raises InsufficientOperatorsError: If there are mismatched parentheses (can be raised from execute_operation)
    :raises InsufficientOperandsError: If the execute_operation function raises this exception
    :raises InvalidValueForOperatorError: If the execute_operation function raises this exception
    """
    if is_previous_left_parenthesis:
        raise InvalidUseOfOperatorError("Empty parentheses")
    while operator_stack and not is_top_left_parenthesis(operator_stack):
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
    :raises InsufficientOperatorsError: If there are mismatched parentheses
    :raises InvalidValueForOperatorError: If an operator is given invalid value
    """
    num = None
    operator = operator_stack.pop()
    if operator == '(':
        raise InsufficientOperatorsError("Mismatched parentheses")

    func = OPERATORS[operator].get_function()
    if is_unary_operator(operator):
        if not operand_stack:
            if is_right_unary_operator(operator):
                raise InvalidUseOfOperatorError(f"Invalid use of '{operator}' operator")
            if is_left_unary_operator(operator):
                return

        operand = operand_stack.pop()

        try:
            num = func(operand)
        except (ValueError, TypeError) as e:
            raise InvalidValueForOperatorError(e)

        if isinstance(num, float) and num.is_integer():
            num = int(num)

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
        except (ZeroDivisionError, ValueError) as e:
            raise InvalidValueForOperatorError(e)

        if isinstance(num, float) and num.is_integer():
            num = int(num)

    operand_stack.append(round(num, 10))


def handle_operator(operator_stack: list[str], operand_stack: list[int | float], operator: str,
                    previous: str | int | float, is_previous_left_parenthesis: bool):
    """
    Handles the current operator in the expression and updates the operator_stack
    :param operand_stack: list of operands
    :param operator_stack: list of operators
    :param operator: The operator to process
    :param previous: The last character or number handled
    :param is_previous_left_parenthesis: A boolean indicating if the previous character is a left parenthesis
    :raises InvalidUseOfOperatorError: If an operator is used incorrectly
    :raises InvalidValueForOperatorError: If the execute_operation function raises this exception
    :raises InsufficientOperandsError: If the execute_operation function raises this exception
    :raises InsufficientOperatorsError: If the execute_operation function raises this exception
    """
    if is_left_unary_operator(previous) and operator != '-' and not is_previous_left_parenthesis:
        raise InvalidUseOfOperatorError(f"Operator '{previous}' needs to be next to a number or parentheses")

    if operator == '-':
        if previous is None or is_previous_left_parenthesis:
            operator = "unaryMinus"
        elif not is_right_unary_operator(previous) and not is_number(previous):
            if previous == "unaryMinus":
                operator = "unaryMinus"
            else:
                operator = "numberMinus"

    if is_right_unary_operator(operator):
        if is_previous_left_parenthesis or not (is_number(previous) or is_right_unary_operator(previous)):
            raise InvalidUseOfOperatorError(f"Operator '{operator}' should be to the right of a number")

    if is_left_unary_operator(operator):
        if is_number(previous) or is_right_unary_operator(previous):
            if is_previous_left_parenthesis:
                raise InsufficientOperatorsError("Not enough operators for a binary operation")
            else:
                raise InvalidUseOfOperatorError(f"Operator '{operator}' should be to the left of a number")

        operator_stack.append(operator)
        return

    if is_binary_operator(operator):
        if is_previous_left_parenthesis:
            raise InsufficientOperandsError(f"Not enough operands for binary operation ('{operator}')")

    while operator_stack and not is_top_left_parenthesis(operator_stack) and OPERATORS[
        operator_stack[-1]].get_precedence() >= OPERATORS[operator].get_precedence():
        execute_operation(operand_stack, operator_stack)

    operator_stack.append(operator)


def get_number(expression: str, index: int) -> tuple[int, int]:
    """
    Finds the number in the index place in the expression
    :param expression: The expression to find the number in
    :param index: The index where the number is starts
    :return: A tuple containing the number and the index to proceed from
    :raises InvalidNumberFormatError: If the number contains more than one decimal point or if a decimal point is not
    followed or preceded by a digit
    """
    number_ended = False
    dot_appeared = False
    number = expression[index]

    if number == '.':
        if index + 1 < len(expression) and expression[index + 1].isdigit():
            number = '0.'
            dot_appeared = True
        else:
            raise InvalidNumberFormatError("A decimal point must be followed or preceded by a digit")

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
    :raises InvalidValueForOperatorError: If the execute_operation function raises this exception or if the
    handle_operator function raises this exception
    """
    operand_stack = []
    operator_stack = []
    index = 0
    previous = None
    is_previous_left_parenthesis = False
    while index < len(expression):
        char = expression[index]

        if char == ' ' or char == '\t':
            pass
            is_previous_left_parenthesis = False

        elif char.isdigit() or char == '.':
            number, index = handle_number(operand_stack, expression, index, previous)
            previous = number
            is_previous_left_parenthesis = False

        elif is_operator(char):
            handle_operator(operator_stack, operand_stack, char, previous, is_previous_left_parenthesis)
            previous = operator_stack[-1]
            is_previous_left_parenthesis = False

        elif char == '(':
            operator_stack.append(char)
            is_previous_left_parenthesis = True

        elif char == ')':
            handle_right_parenthesis(operator_stack, operand_stack, is_previous_left_parenthesis)
            is_previous_left_parenthesis = False

        else:
            raise UnknownCharacterError(f"Invalid character encountered: {char}")

        index += 1

    while operator_stack:
        execute_operation(operand_stack, operator_stack)

    if not operand_stack:
        raise InsufficientOperandsError("Insufficient operands in the expression")

    return operand_stack.pop()
