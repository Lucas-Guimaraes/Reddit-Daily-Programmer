# https://www.reddit.com/r/dailyprogrammer/comments/zx8vw/9152012_challenge_98_easy_arithmetic_tables/

import operator

#Math table
def arithmetic_tables(symbol, digit):
    mapping = {"+": operator.add,
               "-": operator.sub,
               "/": operator.div,
               "*": operator.mul}
    column = [i for i in range(digit+1)]
    row = [i for i in range(digit+1)]
    arithmetic_symbol = mapping[symbol]

    column_print = column
    column_print = "".join(str(column_print))
    column_print = column_print.replace(',', '')
    column_print = column_print.replace('[', '')
    column_print = column_print.replace(']', '')
    column_print = column_print.replace(' ', '  ')
    line_print = "----" * digit
    line_print += "----"

    print(symbol + "  |  " + column_print)
    print(line_print)

    for x in row:
        iter_row = []
        for y in column:
            if symbol != "/":
                row_use = arithmetic_symbol(x, y)
                iter_row.append(row_use)
            else:
                if y == 0:
                    pass
                else:
                    row_use = arithmetic_symbol(x, y)
                    iter_row.append(row_use)

        iter_row = "".join(str(iter_row))
        iter_row = iter_row.replace(',', '')
        iter_row = iter_row.replace('[', '')
        iter_row = iter_row.replace(']', '')
        iter_row = iter_row.replace(' ', '  ')

        print(str(x) + "  |  " + iter_row)
        
#Loops until user quits
math_table = True
while math_table:
    math = raw_input("Insert your command: ")
    symbol_list = ["+", "-", "*", "/"]
    math = math.split()
    
    if math[0] in symbol_list and math[1].isdigit():
        arithmetic_tables(math[0], int(math[1]))
    
    #Quit case.
    if high == "q" or high == "Q":
        break
    highlight(high)

raw_input("Press enter to exit.")

#Test cases:
#arithmetic_tables('+', 16)
