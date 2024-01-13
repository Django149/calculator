class InvalidNumberFormatError(Exception):
    """Exception raised for invalid number format"""
    pass


class InsufficientOperandsError(Exception):
    """Exception raised when there are not enough operands for an operation"""
    pass


class UnknownCharacterError(Exception):
    """Exception raised when an invalid character is encountered in the expression"""
    pass
