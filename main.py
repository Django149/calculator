def handle_expression(expression: str):
    """
    Handles a given expression
    :param expression: The expression to handle
    """
    pass


def main():
    """
    Main function that gets and processes the user's input
    """
    while True:
        try:
            expression = input('Enter an expression: ')
        except EOFError as e:
            print(e)
            continue
        handle_expression(expression)


if __name__ == '__main__':
    main()
