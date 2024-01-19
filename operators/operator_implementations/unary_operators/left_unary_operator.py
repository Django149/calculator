from operators.operator_types.unary_operator import UnaryOperator


class LeftUnaryOperator(UnaryOperator):
    """
    Represents a left unary operator
    """

    def __init__(self, precedence: int, function):
        """
        Initializes a new LeftUnaryOperator instance
        :param precedence: The precedence of the operator
        :param function: A Function that implements the operation of the operator
        """
        super().__init__(precedence, function)
