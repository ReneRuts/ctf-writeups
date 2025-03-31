import pexpect
import re

def solve_arithmetic(expression):
    expression = expression.replace(" ", "")

    if '+' in expression:
        operands = expression.split('+')
        return int(operands[0]) + int(operands[1])
    elif '-' in expression:
        operands = expression.split('-')
        return int(operands[0]) - int(operands[1])
    elif '*' in expression:
        operands = expression.split('*')
        return int(operands[0]) * int(operands[1])
    elif '/' in expression:
        operands = expression.split('/')
        return int(operands[0]) / int(operands[1])

child = pexpect.spawn('./calculate_me_fast')

while True:
    child.expect(r'Question \d+: .* = ?')
    question = child.after.decode('utf-8')

    if re.search(r'HCTF-FLAG-\w+', question):
        print("Flag found! Stopping the program.")