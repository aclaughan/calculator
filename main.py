import logging
from art import logo

logging.basicConfig(level = logging.DEBUG)


def main():
    print(logo)
    calculator()


def add( number1, number2 ):
    """
    returns the sum of number1 and number2
    """
    return number1 + number2


def subtract( number1, number2 ):
    """
    returns the difference between number1 and number2
    """
    return number1 - number2


def multiply( number1, number2 ):
    """
    returns the product of number1 and number2
    """
    return number1 * number2


def divide( number1, number2 ):
    """
    returns the ratio between number1 and number2
    """
    return number1 / number2


def calculate( question ):
    operations = \
        {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide
            }

    parts = question.split(' ')
    num1 = float(parts[0])
    function = operations[parts[1]]
    num2 = float(parts[2])
    answer = str(function(num1, num2))
    print(f"{question} = {answer}")

    return answer


def next_number( num1 ):
    num2 = input("Input your calculation. e.g. + 32\n  > ")
    return calculate(f"{num1} {num2}")


def calculator():
    question = input("Input your calculation. e.g. 23 * 16\n  > ")
    answer = calculate(question)

    while True:
        user = input(
            "press 'y' to continue calculating\n" \
            "press 'n' for a new calculation\n" \
            "or press 'q' to quit,\n  > ")

        if user == 'y':
            num2 = input("Input your calculation. e.g. + 32\n  > ")
            calculate(f"{answer} {num2}")

        elif user == 'n':
            calculator()
        else:
            exit()


if __name__ == '__main__':
    main()
