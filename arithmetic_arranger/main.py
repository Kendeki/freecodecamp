def comparison(a: list, b: list, o: list) -> str:
    c = []
    for i, j, k in zip(a, b, o):
        i, j = list(i), list(j)
        
        i.append("    ")
        j.append("    ")

        if len(i) > len(j):
            i.insert(0, ' ')
            i.insert(0, ' ')
            while len(j) != len(i):
                j.insert(0, ' ')
            j[0] = k
        else:
            j.insert(0, ' ')
            j.insert(0, k)
            while len(j) != len(i):
                i.insert(0, ' ')
        while len(c) != len(i):
            break



def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems"
    if len(list(filter(lambda x: x[x.index(' ') + 1] not in ['+', '-'], problems))) != 0:
        return "Error: Operator must be '+' or '-'."
    if len(list(filter(lambda x: not(''.join([i for i in x if i not in [' ', '+', '-']]).isnumeric()), problems))) != 0:
        return 'Error: Numbers must only contain digits.'
    if len(list(filter(lambda x: len(x[:x.index(" ")]) > 4 or len(x[x.rindex(" "):]) > 4, problems))) != 0:
        return 'Error: Numbers cannot be more than four digits.'

    top = list(map(lambda x: ''.join([i for i in x[:x.index(" ")]]), problems))
    bottom = list(map(lambda x: ''.join([i for i in x[x.rindex(" ") + 1:]]), problems))
    operators = list(map(lambda x: ''.join([i for i in x[x.index(" ") + 1:x.rindex(" ")]]), problems))
    answer = list(map(lambda x: 
                      str(int(top[x]) - int(bottom[x])) if operators[x] == '-' 
                      else str(int(top[x]) + int(bottom[x])), range(len(problems))))
    


    

print(f'\n{arithmetic_arranger(["1 - 78", "3801 - 2", "45 + 43", "123 + 49"], True)}')

# verificar qual dos numeros e maior
# linhas = len do maior numero + 2
# operador sempre na segunda linha, primeiro elemento
# transformo a e b em lista
# checo len(a) > len(b)
# []
"""
0 0 0 x x x
+ 0 y y y y
- - - - - -
0 0 a b c d

The function will return the correct conversion if the supplied problems are properly formatted, otherwise, 
it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:
If there are too many problems supplied to the function. The limit is five, anything more will return: 'Error: Too many problems.'

The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. 
Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: "Error: Operator must be '+' or '-'."

Each number (operand) should only contain digits. Otherwise, the function will return: 'Error: Numbers must only contain digits.'

Each operand (aka number on each side of the operator) has a max of four digits in width. 
Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'

If the user supplied the correct format of problems, the conversion you return will follow these rules:
There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the 
second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).

Numbers should be right-aligned.

There should be four spaces between each problem.

There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually.


"""