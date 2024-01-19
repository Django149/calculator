class Operator(object):
    """
    Base class for mathematical operator_types
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