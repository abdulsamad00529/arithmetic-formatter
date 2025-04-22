def arithmetic_arranger(problems, show_answers=False):

    if len(problems)>5:
        raise ValueError('Error: Too many problems.')
    
    first_line = []
    second_line = []
    dash_line = []
    answers_line = []

    for problem in problems:
        parts = problem.split()
        if len(parts) !=3:
            raise ValueError('Error: Invalid Format.')
        num1, operator, num2 = parts

        if operator not in ['+','-']:
            raise ValueError('Error: Operator must be '+' or '-'.')
        if not num1.isdigit() or not num2.isdigit():
            raise ValueError('Error: Numbers must only contain digits.') 
        if len(num1) > 4 or len(num2) > 4:
            raise ValueError('Error: Numbers cannot me more than four digits.')
        width = max(len(num1),len(num2)) + 2
        first_line.append(num1.rjust(width))
        second_line.append(operator + num2.rjust(width- 1))
        dash_line.append('-' * width)

        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answers_line.append(answer.rjust(width))

    arranged_problems = (
        '    '.join(first_line) +'\n' +
        '    '.join(second_line) + '\n' +
        '    '.join(dash_line)
    )
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers_line)

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)}')

print(f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)}')
