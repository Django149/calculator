import pytest
from calculator_core.calculator import evaluate_expression  # Adjust the import based on your module structure
from calculator_core.calculator_errors.invalid_number_format_error import InvalidNumberFormatError
from calculator_core.calculator_errors.insufficient_operators_error import InsufficientOperatorsError
from calculator_core.calculator_errors.insufficient_operands_error import InsufficientOperandsError
from calculator_core.calculator_errors.unknown_character_error import UnknownCharacterError

from operators.operator_errors.invalid_use_of_operator_error import InvalidUseOfOperatorError


@pytest.mark.parametrize("expression, exception", [
    ("2*^3", InsufficientOperandsError),
    ("!3", InvalidUseOfOperatorError),
    ("5/)", InsufficientOperandsError),
    ("(4+5", InsufficientOperatorsError),
    ("$2+3", InsufficientOperandsError)
])
def test_syntax_error(expression: str,
                      exception: InsufficientOperandsError | InsufficientOperatorsError | InvalidUseOfOperatorError):
    """
    Test simple invalid expressions
    :param expression: The expression to evaluate
    :param exception: Expected exception type for the invalid expression
    """
    with pytest.raises(exception):
        evaluate_expression(expression)


def test_gibberish_string():
    """
    Test gibberish expression
    """
    with pytest.raises(UnknownCharacterError):
        evaluate_expression("gddasrewgf")


def test_empty_string():
    """
    Test empty expression
    """
    with pytest.raises(InsufficientOperandsError):
        evaluate_expression("")


def test_whitespace_string():
    """
    Test whitespace expression
    """
    with pytest.raises(InsufficientOperandsError):
        evaluate_expression("   \t  ")


@pytest.mark.parametrize("expression, expected_result", [
    ("3^2", 9),
    ("1+2", 3),
    ("6-4", 2),
    ("~(4/-2)", 2),
    ("--2*3", 6),
    ("9/5*10", 18),
    ("-5^-2", -0.04),
    ("3@5*3", 12),
    ("6.*1", 6),
    (".2^2", 0.04),
    ("~(~3)", 3),
    ("18/(2+1)", 6),
    ("(2+3)&(4-1)", 3),
    ("4*(2^3)", 32),
    ("(2^2)$2", 4),
])
def test_simple_equations(expression: str, expected_result: int | float):
    """
    Test simple expressions
    :param expression: The expression to evaluate
    :param expected_result: The expected result for the expression
    """
    assert evaluate_expression(expression) == expected_result


@pytest.mark.parametrize("expression, expected_result", [
    ("(1 +2)! + (3@4)^2 - 5", 13.25),
    ("3^2 % 5 + (2+3) @ 2", 12.5),
    ("-(4 + 3^2) +  (2--1)!", -7),
    ("5! + 123# - (2^3 + 12)", 106),
    ("(2^   3 + 12) % 7 * 3 - 2/4", 17.5),
    ("-(3  @ 20) $ 20 - 3^5 % 3", -29),
    ("2 @ 3 @ 4 + 3*(2^2)! / 6", 15.25),
    ("(100)!/99! - - - 2! &    2 * -1.3", 102.6),
    ("(5+4*3) # & -4^(2*2) - 2", 254),
    ("~--6 $ (2+3) + (4+1) % 2^3", 6),
    ("(1+2^3)   # * (3*(2^2)! / 6)", 108),
    ("20 - 3^ 9 % 2 + 4*(3 + 5^2) - 2*3", 123),
    ("(3   /  (50. #!/1$500)    #/ 7) & 0.8", 0.0714285714),
    ("((3+~- - 3 %2 ---5)*-2 +  10)#", 3),
    ("   ~5  $ 4.5 @   3!!# +2 / 2 ", 7.75),
    ("10. / 2 / 9 + ~12 / .1", -119.4444444444),
    ("~(((44*2)# -16 ) /  25  ) +3#!", 6),
    ("(5)-(- 1  ) & 6.5/ 2 / 1! ! !", 5.5),
])
def test_complex_valid_equations(expression: str, expected_result: int | float):
    """
    Test complex expressions
    :param expression: The expression to evaluate
    :param expected_result: The expected result for the expression
    """
    assert evaluate_expression(expression) == expected_result
