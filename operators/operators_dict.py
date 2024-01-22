from operators.operator_implementations.binary_operators.basic_binary_operator import BasicBinaryOperator
from operators.operator_implementations.unary_operators.left_unary_operator import LeftUnaryOperator
from operators.operator_implementations.unary_operators.right_unary_operator import RightUnaryOperator

from operators.operators_math_functions import *

OPERATORS = {"unaryMinus": LeftUnaryOperator(1, negate), "+": BasicBinaryOperator(1, add),
             "-": BasicBinaryOperator(1, subtract), "*": BasicBinaryOperator(2, multiply),
             "/": BasicBinaryOperator(2, divide), "^": BasicBinaryOperator(3, power),
             "%": BasicBinaryOperator(4, modulus), "@": BasicBinaryOperator(5, average),
             "$": BasicBinaryOperator(5, maximum), "&": BasicBinaryOperator(5, minimum),
             "~": LeftUnaryOperator(6, negate), "!": RightUnaryOperator(6, factorial),
             "#": RightUnaryOperator(6, sum_of_digits), "numberMinus": LeftUnaryOperator(10, negate)}
