from calculator_core.calculator import evaluate_expression

from operators.operator_errors.invalid_use_of_operator_error import InvalidUseOfOperatorError
from calculator_core.calculator_errors.invalid_number_format_error import InvalidNumberFormatError
from calculator_core.calculator_errors.insufficient_operators_error import InsufficientOperatorsError
from calculator_core.calculator_errors.insufficient_operands_error import InsufficientOperandsError
from calculator_core.calculator_errors.unknown_character_error import UnknownCharacterError


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
    except ValueError:
        print(f"ValueError: The result of the expression is too big")
    except Exception as e:
        print("Unexpected error: ", e)


def main():
    """
    Main function that gets and processes the user's input
    """
    flag = True
    while flag:
        try:
            expression = input('Enter an expression: ')
            handle_expression(expression)
        except (EOFError, KeyboardInterrupt):
            print("Exiting Calculator...")
            flag = False


if __name__ == '__main__':
    main()
