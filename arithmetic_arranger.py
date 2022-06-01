def arithmetic_arranger(problems, answer = False):
    if len(problems) > 5:
            return "Error: Too many problems."
    
    MARGIN_SPACE = "    "
    first_operands, second_operands, operators = [], [], []
    first_line, second_line, third_line, fourth_line = [], [], [], []

    for problem in problems:
        elements = problem.split()
        first_operands.append(elements[0])
        operators.append(elements[1])
        second_operands.append(elements[2])


    for i in range(len(first_operands)):
        if not (first_operands[i].isdigit() and second_operands[i].isdigit()): return "Error: Numbers must only contain digits."
        if len(first_operands[i]) > 4 or len(second_operands[i]) > 4: return "Error: Numbers cannot be more than four digits."
        if "+" in operators or "-" in operators: continue 
        else:
            return "Error: operators must be '+' or '-'."
            
    #return(first_operands, operators, second_operands)
            
    # build 1st - 3rd
    for i in range(len(first_operands)):
        if len(first_operands[i]) > len(second_operands[i]):    first_line.append(" " * 2 + first_operands[i])
        else:
            first_line.append(" " * (len(second_operands[i]) - len(first_operands[i]) + 2) + first_operands[i])
        if len(second_operands[i]) > len(first_operands[i]):    second_line.append(operators[i] + " " + second_operands[i])
        else:
            second_line.append(operators[i] + " " * (len(first_operands[i]) - len(second_operands[i]) + 1) + second_operands[i])
        third_line.append("-" * (max(len(first_operands[i]), len(second_operands[i])) + 2))

    # build 4th
    for i in range(len(first_operands)):
        ans = eval(first_operands[i] + operators[i] + second_operands[i])
        answer = str(ans)
        if len(answer) > max(len(first_operands), len(second_operands)): fourth_line.append(" " + answer)
        else: 
            fourth_line.append(" " * max(len(first_operands[i]), len(second_operands[i]) - len(answer) + 2) + answer)

        arranged_problems = MARGIN_SPACE.join(first_line) + "\n" + MARGIN_SPACE.join(second_line) + "\n" + MARGIN_SPACE.join(third_line) + "\n" + MARGIN_SPACE.join(fourth_line)
    else:
        arranged_problems = MARGIN_SPACE.join(first_line) + "\n" + MARGIN_SPACE.join(second_line) + "\n" + MARGIN_SPACE.join(third_line) + "\n" + " ".join(fourth_line)
        
    return arranged_problems
