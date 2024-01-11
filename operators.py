class Operator(object):
    """
    Base class for mathematical operators
    """

    def __init__(self, precedence: int, function):
        """
        Initializes a new Operator instance
        :param precedence: The precedence of the operator
        :param function: A Function that implements the operation of the operator
        """
        self.__precedence = precedence
        self.__function = function

    def get_precedence(self):
        """
        Returns the precedence of the operator
        :return: The precedence of the operator
        """
        return self.__precedence

    def get_function(self):
        """
        Returns the function of the operator
        :return: The function of the operator
        """
        return self.__function


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


class UnaryOperator(Operator):
    """
    Base class for unary operators
    """

    def __init__(self, precedence: int, function):
        """
        Initializes a new UnaryOperator instance
        :param precedence: The precedence of the operator
        :param function: A Function that implements the operation of the operator
        """
        super().__init__(precedence, function)


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
