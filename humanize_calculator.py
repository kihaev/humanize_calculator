import re

# constants
list_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
list_dozen = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
list_dozens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
list_big = ["hundred", "thousand", "million", "billion"]
dict_operators = {"+": "plus", "=": "equals", "-": "minus", "/": "divide", "*": "multiply"}
exp = "^[+,\-,=,/,*]*$"


# work with full string
def humanize(str_input):
    list_input = []
    number = ""
    for j in range(len(str_input)):
        if re.match(exp, str_input[j]):
            list_input.append(str_input[j])
        elif not re.match(exp, str_input[j]):
            number += str_input[j]
        elif (j != len(str_input) - 1) and (re.match(exp, str_input[j + 1])) and (not re.match(exp, str_input[j])):
            list_input.append(number)
            number = ""
        elif (not re.match(exp, str_input[j])) and (j == len(str_input) - 1):
            list_input.append(number)
    for key, value in dict_operators.items():
        for m in range(len(list_input)):
            list_input[m] = list_input[m].replace(key, value)
    for i in range(len(list_input)):
        if list_input[i] not in dict_operators.values():
            if len(list_input[i]) < 4:
                list_input[i] = triple(list_input[i])
            elif len(list_input[i]) < 7:
                list_input[i] = triple(list_input[i][:len(list_input[i]) - 3]) + " " + list_big[1] + " " + triple(list_input[i][len(list_input[i]) - 3:])
            elif len(list_input[i]) < 10:
                list_input[i] = triple(list_input[i][:len(list_input[i]) - 6]) + " " + list_big[2] + " " + triple(list_input[i][len(list_input[i]) - 6:len(list_input[i]) - 3]) + " " + list_big[1] + " " + triple(list_input[i][len(list_input[i]) - 3:])
            elif len(list_input[i]) < 13:
                list_input[i] = triple(list_input[i][:len(list_input[i]) - 9]) + " " + list_big[3] + " " + triple(list_input[i][len(list_input[i]) - 9:len(list_input[i]) - 6]) + " " + list_big[2] + " " + triple(list_input[i][len(list_input[i]) - 6:len(list_input[i]) - 3]) + " " + list_big[1] + " " + triple(list_input[i][len(list_input[i]) - 3:])
    return list_input


# work with a part of the string
def triple(number):
    s = ""
    if len(number) == 3:
        for current_digit in range(len(number)):
            if int(number[current_digit]) == 0:
                continue
            elif current_digit == 0:
                s = list_digits[int(number[current_digit])] + " " + list_big[0] + " "
            elif (current_digit == 1) and ((int(number[current_digit]) != 1) or (int(number[current_digit]) == 1 and (int(number[current_digit + 1] == 0)))):
                s += list_dozens[int(number[current_digit]) - 1] + " "
            elif (current_digit == 1) and (int(number[current_digit + 1]) != 0) and (int(number[current_digit]) == 1):
                s += list_dozen[int(number[current_digit] + number[current_digit + 1]) - 11] + " "
            elif (current_digit == 2) and (int(number[current_digit - 1]) != 1):
                s += list_digits[int(number[current_digit])]
    elif len(number) == 2:
        for current_digit in range(len(number)):
            if int(number[current_digit]) == 0:
                continue
            elif (current_digit == 0) and (int(number[current_digit]) != 1) or (int(number[current_digit]) == 1) and (int(number[current_digit + 1]) == 0):
                s = list_dozens[int(number[current_digit]) - 1] + " "
            elif (current_digit == 0) and (int(number[current_digit + 1]) != 0) and (int(number[current_digit]) == 1):
                s += list_dozen[int(number[current_digit] + number[current_digit + 1]) - 11] + " "
            elif (current_digit == 1) and (int(number[current_digit - 1]) != 1):
                s += list_digits[int(number[current_digit])]
    elif len(number) == 1:
        s = list_digits[int(number)]
    return s


# main
if __name__ == '__main__':
    input_status = "Invalid input"
    while input_status != "Okay":
        input_calc = input()
        input_check = input_calc.replace(" ", "")
        if (not input_check) or (not re.match("^[0-9, +, \-, =, /,*,^\s]*$", input_check)):
            print(input_status)
            continue
        else:
            input_status = "Okay"
            print(input_status)
    output = " ".join(humanize(input_check)).rstrip()
    print(re.sub(' +', ' ', output))
