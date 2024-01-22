from calculator_core.calculator import evaluate_expression

from operators.operator_errors.invalid_use_of_operator_error import InvalidUseOfOperatorError
from operators.operator_errors.invalid_value_for_operator_error import InvalidValueForOperatorError
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
        res = evaluate_expression(expression)
        if 'e' in str(float(res)):
            print(float(res))
        else:
            print(res)
    except (InsufficientOperandsError, InvalidNumberFormatError, UnknownCharacterError, InsufficientOperatorsError,
            InvalidUseOfOperatorError, InvalidValueForOperatorError) as e:
        print(f"{e.__class__.__name__}: {e}")
    except (ValueError, OverflowError) as e:
        print(f"{e.__class__.__name__}: The result of the expression is too big")
    except Exception as e:
        print(f"Unexpected error: {e.__class__.__name__}, {e}")


def main():
    """
    Main function that gets and processes the user's input
    """
    flag = True
    while flag:
        try:
            expression = input('Enter an expression: ')
            handle_expression(expression)
        except EOFError:
            print("Exiting Calculator...")
            flag = False


if __name__ == '__main__':
    main()
