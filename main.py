import logging
from art import logo

logging.basicConfig(level = logging.DEBUG)


def main():
    print(logo)
    calculator()

def add(number1, number2):
  """
  returns the sum of number1 and number2
  """
  return number1 + number2

def subtract(number1, number2):
  """
  returns the difference between number1 and number2
  """
  return number1 - number2

def multiply(number1, number2):
  """
  returns the product of number1 and number2
  """
  return number1 * number2

def divide(number1, number2):
  """
  returns the ratio between number1 and number2
  """
  return number1 / number2

operations = \
  {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
  }

def next_number(num1):
  print("Pick an operator ( ", end ='')
  for operation in operations:
    print(f"{operation} ", end='')
  operator = input(")\n  > ")

  num2 = float(input("What is the next number?\n  > "))
  calculate = operations[operator]

  answer = calculate(num1, num2)
  print(f"{num1} {operator} {num2} = {answer}")
  return answer

def calculator():
  num1 = float(input("What is the first number?\n  > "))

  answer = next_number(num1)

  while True:
    user = input(
      "press 'y' to continue calculating\n" \
      "press 'n' for a new calculation\n" \
      "or press 'q' to quit,\n  > ")

    if user == 'y':
      answer = next_number(answer)
    elif user == 'n':
      calculator()
    else:
      exit()

if __name__ == '__main__':
    main()
