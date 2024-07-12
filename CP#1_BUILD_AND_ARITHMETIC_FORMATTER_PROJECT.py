def arithmetic_arranger(problems, show_answers=False):
    # ERROR HANDLING AND BASIS
    if len(problems) > 5: # check specification 1
        return 'Error: Too many problems.'
    else:
        o_o_o_o = [] # overall operand operator operand
        for string in problems:
            if string.find('x') != -1 or string.find('/') != -1:
                return "Error: Operator must be '+' or '-'." # check specification 2
            else:
                s_o_o_o = [] # specific operand operator operand
                empty = ""
                for count in range(len(string)):
                    if not string[count] in "0123456789" and not string[count] in "+-" and not string[count] == ' ':
                        return 'Error: Numbers must only contain digits.' # check specification 3
                    elif string[count].isdigit():
                        empty += string[count]
                        if count == len(string) - 1:
                            s_o_o_o.append(empty)
                        else: pass
                    elif string[count] != ' ':
                        if empty:
                            s_o_o_o.append(empty)
                            empty = ""
                        else: pass
                        s_o_o_o.append(string[count])            
                    else: pass
                if len(s_o_o_o[0]) > 4 or len(s_o_o_o[2]) > 4:
                    return 'Error: Numbers cannot be more than four digits.' # check specification 4
                else:
                    o_o_o_o.append(s_o_o_o)
    # ERROR HANDLING AND BASIS
    # ADDING DASH AND RESULT
    for a_count in range(len(o_o_o_o[:])):
        operand_length = []
        copy_of = o_o_o_o[a_count][:]
        for other_count in range(len(o_o_o_o[a_count][:])):
            operand_length.append(len(o_o_o_o[a_count][other_count]))
        o_o_o_o[a_count].insert(3, (max(operand_length) + 2) * '-')
        if show_answers == True:
            result = eval("".join(copy_of))
            o_o_o_o[a_count].insert(4, str(result))
        else: pass
    # ADDING DASH AND RESULT
    # CORRECT OPERAND OPERATOR OPERAND AND RESULT ARRANGEMENT
    for member in o_o_o_o[:]:
        concatenation = member[2]
        operator = member[1]
        update_string = operator + (len(member[3]) - len(concatenation) - 1) * ' ' + member[2]
        member[1] = update_string
        member.pop(2)
        adding_initiation = (len(member[2]) - len(member[0])) * ' '
        update_initiation = adding_initiation + member[0]
        member[0] = update_initiation
        if show_answers == True:
            adding_result = (len(member[2]) - len(member[3])) * ' '
            update_result = adding_result + member[3]
            member[3] = update_result
        else: pass
    # CORRECT OPERAND OPERATOR AND OPERAND ARRANGEMENT
    # TAB ADDITION
    for counter_another in range(len(o_o_o_o[:])):
        if counter_another != 0:
            for count_other in range(len(o_o_o_o[counter_another])):
                string_and_tab = "    " + o_o_o_o[counter_another][count_other]
                o_o_o_o[counter_another][count_other] = string_and_tab
    # TAB ADDITION
    # MATRIX TRANSPOSE
    transpose_matrix = [list(row) for row in zip(*o_o_o_o)]
    # MATRIX TRANSPOSE
    # NEW LINE ADDITION
    new_line_limit = len(transpose_matrix)
    count_start = 0
    while count_start < new_line_limit - 1:
        transpose_matrix[count_start].append('\n')
        count_start += 1
    concatenation_string = []
    for string_to_concatenate in transpose_matrix:
        concatenation_string.append("".join(string_to_concatenate))
    # NEW LINE ADDITION
    return "".join(concatenation_string)

print(f'{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40"], True)}')