from operators.operator_types.operator import Operator


class UnaryOperator(Operator):
    """
    Base class for unary operator_types
    """

    def __init__(self, precedence: int, function):
        """
        Initializes a new UnaryOperator instance
        :param precedence: The precedence of the operator
        :param function: A Function that implements the operation of the operator
        """
        super().__init__(precedence, function)
