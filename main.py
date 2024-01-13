from errors import InvalidNumberFormatError, InsufficientOperandsError, UnknownCharacterError


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


def handle_number(operand_stack: list[int | float], expression: str, index: int) -> tuple[int, int]:
    """
    Finds the number in the index place in the expression and insert the result into the operand_stack
    :param operand_stack: list of operands
    :param expression: The expression to find the number in
    :param index: The index where the number starts
    :return: A tuple containing the number and the index to proceed from
    :raises InvalidNumberFormatError: if the get_number function raises this exception
    """
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
    :raises InsufficientOperandsError: If there are not enough operands in the expression
    """
    operand_stack = []
    index = 0
    while index < len(expression):
        char = expression[index]

        if char == ' ' or char == '\t':
            pass

        elif char.isdigit():
            number, index = handle_number(operand_stack, expression, index)

        else:
            raise UnknownCharacterError(f"Invalid character encountered: {char}")

        index += 1

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
    except (InsufficientOperandsError, InvalidNumberFormatError, UnknownCharacterError) as e:
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
