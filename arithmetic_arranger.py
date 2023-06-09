def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    arranged_problems = ''
    top = ''
    bottom = ''
    separator_line = ''
    result_line = ''
   
    for problem in problems:
        num1, sign, num2 = problem.split()
        if not (sign == '+' or sign == '-'):
            return "Error: Operator must be '+' or '-'."
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        if (len(num1) > 4 or len(num2) > 4):
            return "Error: Numbers cannot be more than four digits."
        max_length = max(len(num1), len(num2))
        formatted_num1 = num1.rjust(max_length + 2)
        formatted_num2 = sign + num2.rjust(max_length + 1)
        top += formatted_num1 + "   "
        bottom += formatted_num2 + "   "
        result = eval(num1 + sign + num2)
        formatted_result = str(result).rjust(max_length + 2)
        line = '-' * (max_length + 2)
        separator_line += line + "   "
        result_line += formatted_result + "   "
    arranged_problems += top.rstrip() + '\n'
    arranged_problems += bottom.strip() + '\n'
    arranged_problems += separator_line.strip() + '\n'
    arranged_problems += result_line.rstrip() + '\n' 
    if solve:
        return arranged_problems
    return arranged_problems
result = arithmetic_arranger(["3801 - 2", "123 + 49"])
print(result)


