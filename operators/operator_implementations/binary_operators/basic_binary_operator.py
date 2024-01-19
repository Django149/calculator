from operators.operator_types.binary_operator import BinaryOperator


class BasicBinaryOperator(BinaryOperator):
    """
    Represents a basic binary operator
    """

    def __init__(self, precedence: int, function):
        """
        Initializes a new BinaryOperator instance
        :param precedence: The precedence of the operator
        :param function: A Function that implements the operation of the operator
        """
        super().__init__(precedence, function)
