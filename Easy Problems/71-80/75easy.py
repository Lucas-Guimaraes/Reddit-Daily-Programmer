#https://www.reddit.com/r/dailyprogrammer/comments/wfhua/7122012_challenge_75_easy_function_transformation/

#This is made to transform text input, so I did not change it around
#It's mostly a bunch of string formatting to get it exact
#math_exp was important to convert everything
#f, body is how the string splits so that the f (function) can be separate from the body

def transform(inp_str):
    (f, body) = inp_str.split('=')
    math_exp = ['exp', 'log','sqrt','abs','sin','cos','tan']
    for op in math_exp:
        body = body.replace(op, "f"+op+"f")
    
    f_i = f.index('(')
    f_name = f[:f_i]
    first_line = 'float ' + f_name + '(float x,float y)\n'
    second_line = '{\n'
    third_line = '    return ' + body + ';\n'
    fourth_line = '}'
    final_line = (first_line + second_line + third_line + fourth_line)
    return final_line

print(transform('L0(x,y)=abs(x)+abs(y)'))
print('\n')
print(transform('Hey(x,y)=sqrt(x)+sqrt(y)'))

raw_input("\n Press enter to exit.")

#print {float L0(float x, float y)/n{/nreturn fabsf(x)+fabsf(/y);}