def arithmetic_arranger(problems, answer=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    MARGIN_SPACE = "    "
    SINGLE_SPACE = " "
    SEPARATOR_CHAR = "-"

    first_operands, second_operands, operators = [], [], []
    first_line, second_line, third_line, fourth_line = [], [], [], []

    for problem in problems:
        [first, operator, second] = problem.split(' ')
        first_operands.append(first)
        operators.append(operator)
        second_operands.append(second)

    for i in range(len(operators)):
        if not (first_operands[i].isdigit() and second_operands[i].isdigit()):
            return "Error: Numbers must only contain digits."
        if len(first_operands[i]) > 4 or len(second_operands[i]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if not ("+" in operators[i] or "-" in operators[i]):
            return "Error: Operator must be \'+\' or \'-\'."

        ans = str(eval(first_operands[i] + operators[i] + second_operands[i]))

        len_1 = len(first_operands[i])
        len_2 = len(second_operands[i])
        len_3 = len(ans)

        repeat_1 = 2 if len_1 > len_2 else ((len_2 - len_1) + 2)
        repeat_2 = ((len_1 - len_2) if len_1 > len_2 else 0) + 1
        repeat_3 = max((len_1 + repeat_1), (len_2 + repeat_2 + 1))
        repeat_4 = repeat_3 - len_3

        first_line.append(SINGLE_SPACE * repeat_1 + first_operands[i])
        second_line.append(operators[i] + SINGLE_SPACE * repeat_2 + second_operands[i])
        third_line.append(SEPARATOR_CHAR * repeat_3)
        fourth_line.append(SINGLE_SPACE * repeat_4 + ans)

    return MARGIN_SPACE.join(first_line) + \
        "\n" + MARGIN_SPACE.join(second_line) + \
        "\n" + MARGIN_SPACE.join(third_line) + \
        "{}".format(answer and "\n" + MARGIN_SPACE.join(fourth_line) or "")

if __name__ == '__main__':
    print(arithmetic_arranger(['3801 - 2', '123 + 49']) + '\n')
    print(arithmetic_arranger(['1 + 2', '1 - 9380']) + '\n')
    print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']) + '\n')
    print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))
