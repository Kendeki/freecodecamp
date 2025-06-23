def arithmetic_arranger(problems, show_answers=False):
    
    if len(problems) > 5:
        return "Error: Too many problems."
    if len(list(filter(lambda x: x[x.index(' ') + 1] not in ['+', '-'], problems))) != 0:
        return "Error: Operator must be '+' or '-'."
    if len(list(filter(lambda x: not(''.join([i for i in x if i not in [' ', '+', '-']]).isnumeric()), problems))) != 0:
        return 'Error: Numbers must only contain digits.'
    if len(list(filter(lambda x: len(x[:x.index(" ")]) > 4 or len(x[x.rindex(" ") + 1:]) > 4, problems))) != 0:
        return 'Error: Numbers cannot be more than four digits.'
    
    top = list(map(lambda x: ''.join([i for i in x[:x.index(" ")]]), problems))
    bottom = list(map(lambda x: ''.join([i for i in x[x.rindex(" ") + 1:]]), problems))
    operators = list(map(lambda x: ''.join([i for i in x[x.index(" ") + 1:x.rindex(" ")]]), problems))
    answer = list(map(lambda x: 
                      str(int(top[x]) - int(bottom[x])) if operators[x] == '-' 
                      else str(int(top[x]) + int(bottom[x])), range(len(problems))))
    
    dots = ['-' * i for i in [len(top[j]) + 2 if len(top[j]) > len(bottom[j]) else len(bottom[j]) + 2 for j in range(len(top))]]
    top = [" " * 2 + top[i] if len(top[i]) > len(bottom[i]) else " " * (len(bottom[i]) + 2 - len(top[i])) + top[i] for i in range(len(top))]
    bottom = [operators[i] + " " + bottom[i] if len(bottom[i]) > len(top[i].lstrip()) else operators[i]+ " " * (len(top[i].lstrip()) + 1 - len(bottom[i])) + bottom[i] for i in range(len(bottom))]
    answer = [" " * (len(top[i]) - len(answer[i])) + answer[i] if len(top[i]) > len(bottom[i]) else " " * (len(bottom[i]) - len(answer[i])) + answer[i] for i in range(len(top))]
    
    for i in range(2*len(top) - 1):
        if i % 2 != 0:
            top.insert(i, "    ")
            bottom.insert(i, "    ")
            answer.insert(i, "    ")
            dots.insert(i, "    ")
    if not show_answers:
        return f"{''.join(top)}\n{''.join(bottom)}\n{''.join(dots)}"
    
    return f"{''.join(top)}\n{''.join(bottom)}\n{''.join(dots)}\n{''.join(answer)}"