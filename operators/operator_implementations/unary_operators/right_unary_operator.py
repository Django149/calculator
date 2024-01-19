from operators.operator_types.unary_operator import UnaryOperator


class RightUnaryOperator(UnaryOperator):
    """
    Represents a right unary operator
    """

    def __init__(self, precedence: int, function):
        """
        Initializes a new RightUnaryOperator instance
        :param precedence: The precedence of the operator
        :param function: A Function that implements the operation of the operator
        """
        super().__init__(precedence, function)
