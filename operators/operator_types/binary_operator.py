from operators.operator_types.operator import Operator


class BinaryOperator(Operator):
    """
    Represents a binary operator
    """

    def __init__(self, precedence: int, function):
        """
        Initializes a new BinaryOperator instance
        :param precedence: The precedence of the operator
        :param function: A Function that implements the operation of the operator
        """
        super().__init__(precedence, function)
